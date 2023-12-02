from typing import Any, Callable

from tasks.grpc_services.permission import check_permission


def is_admin_user(view_func: Callable) -> Callable:
    def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
        token = request.COOKIES.get("access_token")

        role = check_permission(token)
        print(role)
        # todo обработать здесь роль

        return view_func(obj, request, *args, **kwargs)

    return wrapper
