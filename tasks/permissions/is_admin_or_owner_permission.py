from typing import Any, Callable

from django.db.models import QuerySet

from tasks.permissions.base_permissions import BasePermissions


def is_admin_or_owner_user(queryset: QuerySet) -> Any:
    """ONLY FOR 'PUT', 'PATCH', 'DELETE' METHODS"""

    def decorator(view_func: Callable) -> Callable:
        def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            model = queryset.model
            BasePermissions().is_admin_or_owner(request, model, *args, **kwargs)
            return view_func(obj, request, *args, **kwargs)

        return wrapper

    return decorator
