from typing import Any
import pika

# testing using a local rabbit mq
connection = pika.BlockingConnection(pika.BaseConnection("localhost"))

channel = connection.channel()

# create a queue for queries to be sent to 
channel.queue_declare("sqlquery")

# testing with basic publishing 
def send_through_rabbitmq(data: Any):
    channel.basic_publish(
            exchange='', 
            routing_key='hello',
            body=data
            )
    channel.close()


