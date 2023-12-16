import pika

from config.settings import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_USER


def test() -> None:
    credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
    channel.queue_declare(queue="events", durable=True)
    # сообщения, отправленные в обменник notifications с роутом event-notification, будут доставлены в очередь events
    channel.queue_bind(exchange="notifications", queue="events", routing_key="event-notification")

    channel.basic_publish(exchange="notifications", routing_key="event-notification", body="Hello World!")

    connection.close()
