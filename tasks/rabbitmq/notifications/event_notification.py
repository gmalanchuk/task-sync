from typing import Any, Callable

from django.db.models import QuerySet

from config.settings import logger
from tasks.grpc_services.user import get_user_info
from tasks.rabbitmq.producers import producer_event_notification


def event_notification(queryset: QuerySet) -> Any:
    """ONLY FOR 'POST', 'PUT', 'PATCH', 'DELETE' METHODS"""

    def decorator(view_func: Callable) -> Callable:
        def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            if request.method in ("POST", "PUT", "PATCH", "DELETE"):
                response = view_func(obj, request, *args, **kwargs)
                response_data = response.data

                access_token = request.COOKIES.get("access_token")
                user_info = get_user_info(token=access_token)
                title = response_data["title"]

                is_owner = False
                if response_data["owner_id"] == user_info["user_id"]:
                    is_owner = True

                model_name = queryset.model.__name__.lower()

                producer_event_notification(
                    username=user_info["username"],
                    title=title,
                    email=user_info["email"],
                    role=user_info["role"],
                    is_owner=is_owner,
                    http_method=request.method,
                    model_name=model_name,
                )

                return response
            else:
                logger.error(
                    "The event_notification decorator can only be used in the POST, PUT, PATCH, DELETE methods"
                )

        return wrapper

    return decorator
