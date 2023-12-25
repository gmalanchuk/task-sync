from typing import Any

from config.celery import celery_app
from tasks.rabbitmq.notifications import calendar_notification


@celery_app.task(bind=True)
def celery_calendar_notification(self: Any, obj_id: int, owner_username: str, model_name: str) -> None:
    calendar_notification(obj_id=obj_id, owner_username=owner_username, model_name=model_name)
