import pandas as pd
import pika

data = []

def callback(ch, method, properties, body):
    row = eval(body.decode("utf-8"))  # convert string back to dict
    data.append(row)
    if len(data) % 1000 == 0:  # every 1000 rows
        df = pd.DataFrame(data)
        print(df.tail(5))  # show last 5 rows

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue
channel.queue_declare(queue='electricity')

# Consume messages
channel.basic_consume(queue='electricity', on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
