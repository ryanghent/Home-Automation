import paho.mqtt.client as mqtt
import time
import datetime

threshold = 600                         # Threshold for LDR potential divider
ontime = 17                            # After 17:00 hrs the lamp can be on
offtime = 22                           # After 22:00 hrs the lamp will be off
state = 'OFF'

############ Callbacks #####
def on_message(client, userdata, message):
    if message.topic == "bedroom/sensor/light": #Current light value

        global state    #linking the shadow variable inside the callback to the global version
        hour = int(datetime.datetime.now().hour)    #Update the current time
        print hour

        if threshold > int(message.payload.decode("utf-8")) and hour < offtime and hour > ontime:
            #if the current light value is darker (greater) than the threshold and
            #it is in the evening (between 5pm and 10pm), then turn the light on
            state = 'ON'
        else:
            state = 'OFF'
            #otherwise turn it off

def on_log(client, userdata, level, buf):
    print("log: ",buf)

########################################
broker_address="192.168.1.XX" #Locally hosted from my Raspberry pi
#broker_address="test.mosquitto.org" #Externally hosted from Mosquitto. Comment in/out as needed
print("creating new instance")
client = mqtt.Client("") #create new instance, blank ID means broker can re-assign as needed
client.on_message=on_message #attach function to callback
#client.on_log=on_log        #attach logging callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","bedroom/sensor/light")
client.subscribe("bedroom/sensor/light")

while True:
    time.sleep(10)      # wait
    client.loop(0.1)    #New loop implementation, avoiding broken pipe error as cannot publish from same client.
    client.publish("bedroom/lamp/cmnd/POWER1",state) #Publish the message
