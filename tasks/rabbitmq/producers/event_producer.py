from tasks.rabbitmq.connection import ConnectionToRabbitMQ


def producer_event_notification(username: str, title: str) -> None:
    with ConnectionToRabbitMQ() as (channel, connection):
        channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
        channel.queue_declare(queue="events", durable=True)
        # сообщения, отправленные в обменник notifications с роутом event-notification будут отправлены в очередь events
        channel.queue_bind(exchange="notifications", queue="events", routing_key="event-notification")

        channel.basic_publish(
            exchange="notifications", routing_key="event-notification", body=str({"username": username, "title": title})
        )
