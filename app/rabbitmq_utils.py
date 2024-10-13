# rabbitmq_utils.py
import pika


def get_rabbitmq_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return channel


def send_message(queue_name: str, message: str):
    channel = get_rabbitmq_channel()
    # Declare a queue in case it doesn't exist
    channel.queue_declare(queue=queue_name, durable=True)

    # Send message
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    # Close the connection
    channel.close()
