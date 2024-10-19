import aio_pika
import asyncio

from rabbitmq_connection import AsyncRabbitMQConnection


# Функция обратного вызова для обработки полученных сообщений
async def callback(message: aio_pika.IncomingMessage):
    async with message.process():
        print(f" [x] Received {message.body.decode()}")
        # Симуляция длительного выполнения
        await asyncio.sleep(10)  # Ожидание 5 секунд (симуляция длительной обработки)
        print(" [x] Done processing the message.")

# Асинхронная функция для получения сообщений из очереди
async def consume():
    rabbit_connection = AsyncRabbitMQConnection()
    await rabbit_connection.connect()
    channel = await rabbit_connection.get_channel()

    queue = await channel.declare_queue("json_queue")
    await queue.consume(callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume())
    loop.run_forever()
