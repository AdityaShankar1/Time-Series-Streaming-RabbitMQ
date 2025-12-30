import csv, time
import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='electricity')

# Stream dataset rows into RabbitMQ
with open("/Users/adityashankar/Downloads/electricity_dataset.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        channel.basic_publish(exchange='',
                              routing_key='electricity',
                              body=str(row))
        time.sleep(0.001)  # simulate 1 ms per row

connection.close()
print("Finished streaming dataset ✅")
