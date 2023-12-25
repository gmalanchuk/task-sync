from tasks.rabbitmq.connection import ConnectionToRabbitMQ


def producer_calendar_notification(title: str, owner_username: str, email: str, deadline: str, model_name: str) -> None:
    with ConnectionToRabbitMQ() as (channel, connection):
        channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
        channel.queue_declare(queue="calendar", durable=True)
        channel.queue_bind(exchange="notifications", queue="calendar", routing_key="calendar-notification")

        channel.basic_publish(
            exchange="notifications",
            routing_key="calendar-notification",
            body=str(
                {
                    "title": title,
                    "owner_username": owner_username,
                    "email": email,
                    "deadline": deadline,
                    "model_name": model_name,
                }
            ),
        )
