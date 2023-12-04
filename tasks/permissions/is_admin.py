from typing import Any, Callable

from tasks.permissions.checks import Checks


def is_admin_user(view_func: Callable) -> Callable:
    def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
        Checks().is_admin(request, *args, **kwargs)
        return view_func(obj, request, *args, **kwargs)

    return wrapper
