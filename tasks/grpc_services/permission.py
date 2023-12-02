import grpc

from config.settings import AUTHENTICATION_SERVICE_DOMAIN, GRPC_PORT
from tasks.protos.permission_pb2 import PermissionRequest
from tasks.protos.permission_pb2_grpc import PermissionStub


def check_permission(token: str) -> None | str:
    with grpc.insecure_channel(f"{AUTHENTICATION_SERVICE_DOMAIN}:{GRPC_PORT}") as channel:
        stub = PermissionStub(channel)
        try:
            response = stub.CheckPermission(PermissionRequest(token=token))
            return response.role
        except grpc.RpcError as e:
            error_message = e.details()
            print(f"Error Message: {error_message}")

    return None
