from tasks.rabbitmq.connection import ConnectionToRabbitMQ


def producer_calendar_notification(
    title: str, owner_name: str, email: str, executor_name: str, deadline: str, model_name: str
) -> None:
    with ConnectionToRabbitMQ() as channel:
        channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
        channel.queue_declare(queue="calendar", durable=True)
        channel.queue_bind(exchange="notifications", queue="calendar", routing_key="calendar-notification")

        channel.basic_publish(
            exchange="notifications",
            routing_key="calendar-notification",
            body=str(
                {
                    "title": title,
                    "owner_name": owner_name,
                    "email": email,
                    "executor_name": executor_name,
                    "deadline": deadline,
                    "model_name": model_name,
                }
            ),
        )
