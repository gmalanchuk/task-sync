from django.apps import apps

from tasks.rabbitmq.producers import producer_calendar_notification


def calendar_notification(obj_id: int, owner_name: str, email: str, executor_name: str, model_name: str) -> None:
    model = apps.get_model(app_label="tasks", model_name=model_name)
    obj_model = model.objects.get(id=obj_id)
    deadline = str(obj_model.deadline)[:-6]
    producer_calendar_notification(
        title=obj_model.title,
        owner_name=owner_name,
        email=email,
        executor_name=executor_name,
        deadline=deadline,
        model_name=model_name,
    )
