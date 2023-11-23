import grpc

from protos import helloworld_pb2, helloworld_pb2_grpc


def run() -> None:
    print("Will try to greet world ...")
    with grpc.insecure_channel("authentication:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)
