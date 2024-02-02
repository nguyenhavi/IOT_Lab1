import sys
from Adafruit_IO import MQTTClient
import random
import time

AIO_FEED_IDs = ["button1"]
AIO_USERNAME = "nguyenha25012002"
AIO_KEY = "aio_Yziq65NmpxNUPkWit5QeALB1RMsX"

def connected(client):
    print("Connect successfully ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe successfully ...")

def disconnected(client):
    print("Disconnect ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Receive data: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    client.publish("button1", random.randint(0, 1))
    time.sleep(5)
    pass