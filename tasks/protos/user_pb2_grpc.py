# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tasks.protos import user_pb2 as tasks_dot_protos_dot_user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckUserToken = channel.unary_unary(
                '/user.User/CheckUserToken',
                request_serializer=tasks_dot_protos_dot_user__pb2.UserRequestToken.SerializeToString,
                response_deserializer=tasks_dot_protos_dot_user__pb2.UserResponse.FromString,
                )
        self.CheckUserID = channel.unary_unary(
                '/user.User/CheckUserID',
                request_serializer=tasks_dot_protos_dot_user__pb2.UserRequestID.SerializeToString,
                response_deserializer=tasks_dot_protos_dot_user__pb2.UserResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckUserToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckUserToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckUserToken,
                    request_deserializer=tasks_dot_protos_dot_user__pb2.UserRequestToken.FromString,
                    response_serializer=tasks_dot_protos_dot_user__pb2.UserResponse.SerializeToString,
            ),
            'CheckUserID': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckUserID,
                    request_deserializer=tasks_dot_protos_dot_user__pb2.UserRequestID.FromString,
                    response_serializer=tasks_dot_protos_dot_user__pb2.UserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckUserToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/CheckUserToken',
            tasks_dot_protos_dot_user__pb2.UserRequestToken.SerializeToString,
            tasks_dot_protos_dot_user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/CheckUserID',
            tasks_dot_protos_dot_user__pb2.UserRequestID.SerializeToString,
            tasks_dot_protos_dot_user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
