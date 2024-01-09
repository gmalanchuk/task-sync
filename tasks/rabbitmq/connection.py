import pika

from config.settings import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_USER, logger


class ConnectionToRabbitMQ:
    def __enter__(self) -> pika.channel:
        credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
        )
        self.channel = self.connection.channel()
        logger.info("Rabbitmq connection open")
        return self.channel

    def __exit__(self, *args: tuple) -> None:
        logger.info("Rabbitmq connection closed")
        self.connection.close()
