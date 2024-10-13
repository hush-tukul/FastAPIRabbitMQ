# consumer.py
import pika


def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")


def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the same queue we used for sending messages
    channel.queue_declare(queue='hello_queue', durable=True)

    # Set up a consumer and start listening
    channel.basic_consume(queue='hello_queue', on_message_callback=callback, auto_ack=True)

    print("Waiting for messages. To exit, press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    consume_messages()
