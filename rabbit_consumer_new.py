import pika
from data_develop import develop_callback
from config import (
    host, 
    queue, 
    exchange
)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host)
)

channel = connection.channel()
channel.exchange_declare(
    exchange=exchange, 
    exchange_type='fanout'
)

result = channel.queue_declare(
    queue=queue, 
    exclusive=True
)
queue_name = result.method.queue

channel.queue_bind(
    exchange=exchange, 
    queue=queue_name
)

channel.basic_consume(
    queue=queue_name, 
    on_message_callback=develop_callback, 
    auto_ack=True
)
channel.start_consuming()
