import paho.mqtt.client as mqtt
import time
import datetime
import psutil


ontime = 9                            # After 9:00 hrs the laptop can be charging
offtime = 23                           # After 23:00 hrs the laptop will not be charging (it has an annoying charging light)
state = 'OFF'

############ Callbacks #####
def check(ontime,offtime):
    hour = int(datetime.datetime.now().hour)
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    global state

    if state == 'ON' and percent > 80:    #When Charging, stop Charging at 80% to maximise battery life
        state = 'OFF'

    elif state == 'OFF' and percent < 20 and hour < offtime and hour > ontime:
        #Start charging at 20% for optimal battery life in the long term. But don't charge at night because of the charging light
            state = 'ON'

def on_log(client, userdata, level, buf):
    print("log: ",buf)

########################################
broker_address="192.168.1.XX" #Locally hosted from my Raspberry pi
#broker_address="test.mosquitto.org" #Externally hosted from Mosquitto. Comment in/out as needed
print("creating new instance")
client = mqtt.Client("") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start()

while True:
    time.sleep(10) # wait
    check(ontime,offtime)
    client.publish("bedroom/lamp/cmnd/POWER1",state) #Publish the message
