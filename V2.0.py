import paho.mqtt.client as mqtt
import time
#from pathlib import Path Not sure where files will be made if run on startup

############ Callbacks #####
def on_message(client, userdata, message):
    if message.topic == "bedroom/sensor/light": #Store the current light value
        L = open('lightvalues.txt','a')
        L.write(', ' + str(message.payload.decode("utf-8")))
        L.close()

    elif message.topic == "bedroom/sensor/humidity": #Store the current humidity value
        H = open('humidityvalues.txt','a')
        H.write(', ' + str(message.payload.decode("utf-8")))
        H.close()
    elif message.topic == "bedroom/sensor/temperature": #Store the current humidity value
        T = open('temperaturevalues.txt','a')
        T.write(', ' + str(message.payload.decode("utf-8")))
        T.close()


    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

########################################
broker_address="192.168.1.XX" #Locally hosted from my Raspberry pi
#broker_address="test.mosquitto.org" #Externally hosted from Mosquitto. Comment in/out as needed
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","bedroom/sensor")
client.subscribe("bedroom/sensor/light")
client.subscribe("bedroom/sensor/humidity")
client.subscribe("bedroom/sensor/temperature")
while True:
    time.sleep(10) # wait
