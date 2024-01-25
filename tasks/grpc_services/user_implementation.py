from rest_framework.request import Request

from tasks.grpc_services.user import __get_user_info_by_id, __get_user_info_by_token


def get_user_info_by_token(request: Request) -> dict:
    token = request.COOKIES.get("access_token")
    user = __get_user_info_by_token(token)
    return user


def get_user_info_by_id(user_id: int) -> dict:
    user = __get_user_info_by_id(user_id)
    return user
