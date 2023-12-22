from typing import Any, Callable

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from config.settings import logger
from tasks.grpc_services.user import get_user_info
from tasks.rabbitmq.producers import producer_event_notification


def event_notification(queryset: QuerySet) -> Any:
    """ONLY FOR 'POST', 'PUT', 'PATCH', 'DELETE' METHODS"""

    def decorator(view_func: Callable) -> Callable:
        def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            if request.method in ("POST", "PUT", "PATCH", "DELETE"):
                if request.method != "DELETE":
                    response = view_func(obj, request, *args, **kwargs)

                model = queryset.model
                pk = response.data["id"] if request.method == "POST" else kwargs["pk"]
                obj_model = get_object_or_404(model, id=pk)

                access_token = request.COOKIES.get("access_token")
                user_info = get_user_info(token=access_token)

                is_owner = False
                if obj_model.owner_id == user_info["user_id"]:
                    is_owner = True

                if request.method == "DELETE":
                    response = view_func(obj, request, *args, **kwargs)

                producer_event_notification(
                    username=user_info["username"],
                    title=obj_model.title,
                    email=user_info["email"],
                    role=user_info["role"],
                    is_owner=is_owner,
                    http_method=request.method,
                    model_name=model.__name__.lower(),
                )

                return response
            else:
                logger.error(
                    "The event_notification decorator can only be used in the POST, PUT, PATCH, DELETE methods"
                )

        return wrapper

    return decorator
