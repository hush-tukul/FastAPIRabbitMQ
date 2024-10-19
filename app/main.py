from contextlib import asynccontextmanager

import aio_pika
from fastapi import FastAPI, HTTPException
import json
from fastapi.responses import JSONResponse
from threading import Thread
import time
import asyncio

from app.rabbitmq_connection import AsyncRabbitMQConnection
from app.validation import RegistrationConfirmation


# Функция для отправки данных в RabbitMQ
async def send_to_rabbitmq(data):
    rabbit_connection = AsyncRabbitMQConnection()
    channel = await rabbit_connection.get_channel()
    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps(data).encode()),
        routing_key="json_queue"
    )
    print(f"Sent to RabbitMQ: {data}")

# Функция для генерации и отправки JSON каждые 5 секунд
async def generate_json():
    while True:
        # Создаем тестовый JSON-объект
        data = {
            "message": "Hello, World!",
            "timestamp": time.time()
        }
        await send_to_rabbitmq(data)
        await asyncio.sleep(1)  # Отправляем каждую 1 секунду


# Using FastAPI lifespan for startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code: start the background task
    task = asyncio.create_task(generate_json())

    # Yield to start the application
    yield

    # Shutdown code: cancel the background task if needed
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")


app = FastAPI(lifespan=lifespan)
#app = FastAPI()
@app.get("/")
async def root():
    return JSONResponse(content={"message": "Server is running. JSON is being sent to RabbitMQ every 5 seconds."})


@app.post("/register")
async def register_user(confirmation: RegistrationConfirmation):
    data = {
        "email": confirmation.email,
        "message": "Please confirm your registration."
    }

    try:
        await send_to_rabbitmq(data)  # Отправляем данные в RabbitMQ
        return JSONResponse(content={"message": "Confirmation email sent!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send confirmation email.")