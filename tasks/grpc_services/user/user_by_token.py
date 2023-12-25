import re

import grpc

from config.settings import AUTHENTICATION_SERVICE_DOMAIN, GRPC_PORT, grpc_to_http_errors
from tasks.exceptions import CustomAPIException
from tasks.protos.user_pb2 import UserRequestToken
from tasks.protos.user_pb2_grpc import UserStub


def get_user_info_by_token(token: str) -> dict:
    with grpc.insecure_channel(f"{AUTHENTICATION_SERVICE_DOMAIN}:{GRPC_PORT}") as channel:
        stub = UserStub(channel)
        try:
            response = stub.CheckUserToken(UserRequestToken(token=token))
            return {
                "user_id": response.user_id,
                "username": response.username,
                "email": response.email,
                "name": response.name,
                "role": response.role,
            }
        except grpc.RpcError as e:
            error_message = e.details()
            match = re.search(r"<StatusCode\.(\w+).*?>, '(.*?)'", error_message)
            if match:
                status_code, data = match.group(1), match.group(2)
                raise CustomAPIException(detail=data, status_code=grpc_to_http_errors[status_code])

    return {}
