from types import TracebackType
from typing import Optional, Tuple, Type

import pika

from config.settings import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_USER, logger


class ConnectionToRabbitMQ:
    def __enter__(self) -> Tuple[pika.channel, pika.connection]:
        credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
        )
        self.channel = self.connection.channel()
        logger.info("Rabbitmq connection open")
        return self.channel, self.connection

    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], traceback: Optional[TracebackType]
    ) -> None:
        logger.info("Rabbitmq connection closed")
        self.connection.close()
