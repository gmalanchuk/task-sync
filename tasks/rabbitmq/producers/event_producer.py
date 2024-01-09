from tasks.rabbitmq.connection import ConnectionToRabbitMQ


def producer_event_notification(
    name: str, title: str, email: str, is_owner: bool, http_method: str, model_name: str
) -> None:
    with ConnectionToRabbitMQ() as channel:
        channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
        channel.queue_declare(queue="events", durable=True)
        # сообщения, отправленные в обменник notifications с роутом event-notification будут отправлены в очередь events
        channel.queue_bind(exchange="notifications", queue="events", routing_key="event-notification")

        channel.basic_publish(
            exchange="notifications",
            routing_key="event-notification",
            body=str(
                {
                    "name": name,
                    "title": title,
                    "email": email,
                    "is_owner": is_owner,
                    "http_method": http_method,
                    "model_name": model_name,
                }
            ),
        )
