from types import TracebackType
from typing import Optional, Tuple, Type

import pika

from config.settings import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_USER


class ConnectionToRabbitMQ:
    def __enter__(self) -> Tuple[pika.Channel, pika.Connection]:
        credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
        )
        self.channel = self.connection.channel()
        return self.channel, self.connection

    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], traceback: Optional[TracebackType]
    ) -> None:
        self.connection.close()
