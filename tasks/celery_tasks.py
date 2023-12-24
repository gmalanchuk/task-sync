from datetime import datetime
from typing import Any

from config.celery import celery_app


@celery_app.task(bind=True)
def celery_calendar_notification(self: Any, deadline: datetime) -> None:
    print("=====================================")
    print(datetime.utcnow())
    print(deadline)
    print("=====================================")
