from fastapi import FastAPI

from app.rabbitmq_utils import send_message

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    message = f"Hello {name}"

    # Send message to RabbitMQ
    send_message(queue_name='hello_queue', message=message)

    return {"message": message}
