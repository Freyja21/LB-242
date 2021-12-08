from time import sleep
import paho.mqtt.client as mqtt
from tinder_bot_sms import TinderBotSms
import subprocess
import config


def publish(tinder_token):
    client = mqtt.Client()
    client.connect("192.168.249.111",1883,60)
    client.publish("tinder", "hello <3")

    tinder = TinderBotSms(tinder_token)
    tinder.auto_swipe(5)
    for person in tinder.get_persons():
        client.publish("tinder","name: "+ person.name + "type: " +person.type )
        if(person.type == "like"):
   
            subprocess.run(["oled.exe", ":)"])
        else:
            subprocess.run(["oled.exe", ":("])
        sleep(3)
    client.disconnect()