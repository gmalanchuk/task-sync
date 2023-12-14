import re

import grpc

from config.settings import AUTHENTICATION_SERVICE_DOMAIN, GRPC_PORT, grpc_to_http_errors
from tasks.exceptions import CustomAPIException
from tasks.protos.permission_pb2 import RoleUserIDRequest
from tasks.protos.permission_pb2_grpc import PermissionStub


def check_role_and_userid(token: str) -> dict:
    with grpc.insecure_channel(f"{AUTHENTICATION_SERVICE_DOMAIN}:{GRPC_PORT}") as channel:
        stub = PermissionStub(channel)
        try:
            response = stub.CheckRoleUserID(RoleUserIDRequest(token=token))
            return {"role": response.role, "user_id": response.user_id}
        except grpc.RpcError as e:
            error_message = e.details()
            match = re.search(r"<StatusCode\.(\w+).*?>, '(.*?)'", error_message)
            if match:
                status_code, data = match.group(1), match.group(2)
                raise CustomAPIException(detail=data, status_code=grpc_to_http_errors[status_code])

    return {}
