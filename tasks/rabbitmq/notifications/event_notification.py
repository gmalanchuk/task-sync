from typing import Any, Callable

from tasks.grpc_services.user import get_user_info
from tasks.rabbitmq.producers import producer_event_notification


def event_notification(view_func: Callable) -> Callable:
    def wrapper(obj: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
        response = view_func(obj, request, *args, **kwargs)
        response_data = response.data

        access_token = request.COOKIES.get("access_token")
        username = get_user_info(token=access_token)["username"]
        title = response_data["title"]

        producer_event_notification(username=username, title=title)

        return response

    return wrapper
