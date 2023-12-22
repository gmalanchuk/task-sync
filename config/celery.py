import os
import time

from celery import Celery, shared_task


os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="config.settings")

celery_app = Celery(main="config")

celery_app.config_from_object(obj="django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@shared_task
def test1() -> None:
    for i in range(5):
        time.sleep(1)
        print("test1")


@shared_task
def test2() -> None:
    for i in range(5):
        time.sleep(1)
        print("test2")
