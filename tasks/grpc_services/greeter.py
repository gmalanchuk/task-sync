import grpc

from tasks.protos.helloworld_pb2 import HelloRequest
from tasks.protos.helloworld_pb2_grpc import GreeterStub
from tasks.protos.permission_pb2 import PermissionRequest
from tasks.protos.permission_pb2_grpc import PermissionStub


def greeter() -> None:
    print("Will try to greet world ...")
    with grpc.insecure_channel("authentication:50051") as channel:
        stub = GreeterStub(channel)
        response = stub.SayHello(HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


def check_permission() -> None:
    with grpc.insecure_channel("authentication:50051") as channel:
        stub = PermissionStub(channel)
        response = stub.CheckPermission(
            PermissionRequest(
                token="""eydhbGcnOiAnSFMyNTYnLCAndHlwJzogJ0pXVCd9.
                      eyd1c2VyX2lkJzogMSwgJ2V4cGlyYXRpb25fdGltZSc6ICcyMDIzLTExLTI1IDE4OjU4OjQ5J30=.
                      d3e7c2b9f69029dd6c90eb84e6a81481cd98ca079994f7c3c25618e220ce9f24"""
            )
        )
    print("====================================")
    print()
    print(response.role)
    print()
    print("====================================")
