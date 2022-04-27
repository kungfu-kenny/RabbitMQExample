import pika
from data_develop import develop_callback
from config import host, queue


def develop_consumer_basic():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(
        queue=queue, 
        on_message_callback=develop_callback, 
        auto_ack=True
    )
    channel.start_consuming()


if __name__ == '__main__':
    develop_consumer_basic()