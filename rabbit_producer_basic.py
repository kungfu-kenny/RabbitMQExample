import pika
from time import sleep
from data_develop import develop_random_data
from config import (
    host, 
    queue,
    index_end,
    index_begin
)


with pika.BlockingConnection(
    pika.ConnectionParameters(host=host)
) as connection:

    channel = connection.channel()
    channel.queue_declare(queue=queue)
    for i in range(index_begin, index_end):
        channel.basic_publish(
            exchange='', 
            routing_key='hello', 
            body=develop_random_data(i)
        )
        print("Sent Index:", i)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        sleep(0.02)