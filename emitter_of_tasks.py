# Arsh Kandola 
import pika
import sys
import webbrowser
import csv
import struct
from datetime import datetime
import time

def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    ans = input("Would you like to monitor RabbitMQ queues? y or n ")
    print()
    if ans.lower() == "y":
        webbrowser.open_new("http://localhost:15672/#/queues")
        

def send_message(host: str, queue_name: str, message: bytes):
    

    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a durable queue
        ch.queue_declare(queue=queue_name, durable=True)
        # use the channel to publish a message to the queue
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)
        # print a message to the console for the user
        print(f" [x] Sent message to {queue_name}")
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()


def main():
    """Reads data from CSV file and sends it to RabbitMQ queues."""
    with open("smoker-temps.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for data_row in reader:
            str_timestamp = data_row[0]
            smoker_temp = data_row[1]
            food_a_temp = data_row[2]
            food_b_temp = data_row[3]

            # Convert timestamp string to Unix
            timestamp = datetime.strptime(str_timestamp, "%m/%d/%y %H:%M:%S").timestamp()

            if smoker_temp:
                message = struct.pack('!df', timestamp, float(smoker_temp))
                send_message("localhost", "01-smoker", message)
            
            if food_a_temp:
                message = struct.pack('!df', timestamp, float(food_a_temp))
                send_message("localhost", "02-food-A", message)
            
            if food_b_temp:
                message = struct.pack('!df', timestamp, float(food_b_temp))
                send_message("localhost", "03-food-B", message)
            
            # Wait for 30 seconds between reading rows
            time.sleep(5)


if __name__ == "__main__":  
    offer_rabbitmq_admin_site()
    main()

cd /Users/muffinman/Desktop/STREAMING DATA/streaming-05-smart-smoker
ls
conda activate base
python listening_worker.py
