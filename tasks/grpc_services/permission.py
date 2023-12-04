import re

import grpc

from config.settings import AUTHENTICATION_SERVICE_DOMAIN, GRPC_PORT, grpc_to_http_errors
from tasks.protos.permission_pb2 import PermissionRequest
from tasks.protos.permission_pb2_grpc import PermissionStub


def check_permission(token: str) -> dict | str | None:
    with grpc.insecure_channel(f"{AUTHENTICATION_SERVICE_DOMAIN}:{GRPC_PORT}") as channel:
        stub = PermissionStub(channel)
        try:
            response = stub.CheckPermission(PermissionRequest(token=token))
            return response.role
        except grpc.RpcError as e:
            error_message = e.details()
            match = re.search(r"<StatusCode\.(\w+).*?>, '(.*?)'", error_message)
            if match:
                status_code, data = match.group(1), match.group(2)
                return {"data": data, "status": grpc_to_http_errors[status_code]}

            return None