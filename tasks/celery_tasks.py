from typing import Any

from config.celery import celery_app
from tasks.rabbitmq.notifications import calendar_notification


@celery_app.task(bind=True)
def celery_calendar_notification(
    _: Any, obj_id: int, owner_name: str, email: str, executor_name: str, model_name: str
) -> None:
    calendar_notification(
        obj_id=obj_id,
        owner_name=owner_name,
        email=email,
        executor_name=executor_name,
        model_name=model_name,
    )
