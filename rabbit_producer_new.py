import pika
from time import sleep
from data_develop import develop_random_data
from config import (
    host, 
    queue,
    exchange,
    index_end, 
    index_begin
)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host)
)

channel = connection.channel()
channel.exchange_declare(
    exchange=exchange, 
    exchange_type='fanout'
)

for i in range(index_begin, index_end):
    channel.basic_publish(
        exchange=exchange, 
        routing_key=queue, 
        body=develop_random_data(i)
    )
    print("Sent Index:", i)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    sleep(0.02)

connection.close()