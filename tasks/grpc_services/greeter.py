import grpc

from tasks.protos.helloworld_pb2 import HelloRequest
from tasks.protos.helloworld_pb2_grpc import GreeterStub


def greeter() -> None:
    print("Will try to greet world ...")
    with grpc.insecure_channel("authentication:50051") as channel:
        stub = GreeterStub(channel)
        response = stub.SayHello(HelloRequest(name="you"))
    print("Greeter client received: " + response.message)
