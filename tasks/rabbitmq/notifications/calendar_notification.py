from django.db.models import Model

from tasks.rabbitmq.producers import producer_calendar_notification


def calendar_notification(obj_id: int, owner_username: str, model: Model) -> None:
    obj_model = model.objects.get(id=obj_id)
    deadline = str(obj_model.deadline)[:-6]
    producer_calendar_notification(title=obj_model.title, owner_username=owner_username, deadline=deadline)
