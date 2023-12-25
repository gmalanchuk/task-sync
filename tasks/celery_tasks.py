from typing import Any

from django.apps import apps

from config.celery import celery_app
from tasks.rabbitmq.notifications import calendar_notification


@celery_app.task(bind=True)
def celery_calendar_notification(self: Any, obj_id: int, owner_username: str, model_name: str) -> None:
    model = apps.get_model(app_label="tasks", model_name=model_name)
    calendar_notification(obj_id=obj_id, owner_username=owner_username, model=model)
