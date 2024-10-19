import aio_pika
import asyncio

class AsyncRabbitMQConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AsyncRabbitMQConnection, cls).__new__(cls)
        return cls._instance

    async def connect(self):
        if not hasattr(self, "connection") or self.connection.is_closed:
            self.connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
            self.channel = await self.connection.channel()
            await self.channel.declare_queue("json_queue")

    async def get_channel(self):
        if not hasattr(self, "channel"):
            await self.connect()
        return self.channel

    async def close_connection(self):
        if hasattr(self, "connection") and not self.connection.is_closed:
            await self.connection.close()
