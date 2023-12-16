import pika

from config.settings import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_USER


def test() -> None:
    credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
    print(" [x] Sent 'Hello World!'")
    connection.close()
