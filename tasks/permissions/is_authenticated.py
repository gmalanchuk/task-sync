from typing import Any, Callable

from rest_framework.response import Response

from tasks.grpc_services.permission import check_permission


def is_authenticated_user(view_func: Callable) -> Callable:
    def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
        token = request.COOKIES.get("access_token")
        role_or_error_message = check_permission(token)
        if isinstance(role_or_error_message, dict):
            return Response(data={"detail": role_or_error_message["data"]}, status=role_or_error_message["status"])

        return view_func(obj, request, *args, **kwargs)

    return wrapper
