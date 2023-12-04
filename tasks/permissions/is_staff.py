from typing import Any, Callable

from tasks.permissions.checks import Checks


def is_staff_user(view_func: Callable) -> Callable:
    def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
        Checks().is_staff(request, *args, **kwargs)
        return view_func(obj, request, *args, **kwargs)

    return wrapper
