import paho.mqtt.client as mqtt
import phone_auth_token as auth
from time import sleep
import paho.mqtt.client as mqtt
from tinder_bot_sms import TinderBotSms
import subprocess
import random

phone_number = ''
def on_connect(client, userdata,flags,rc):
    print("connected with result code "+ str(rc))
    client.subscribe("tinder")

def on_connect_oled(client,userdata,flags,rc):
    clientOled.subscribe("tinder/oled")

def on_message(client, userdata, msg):
    if  "00" in msg.payload.decode():
        phone_number = msg.payload.decode()
        log_code = auth.send_otp_code(phone_number)
    else:
        otp_code = msg.payload.decode()
        refresh_token =auth.get_refresh_token(otp_code, phone_number)
        print("Here is your Tinder token: " + str(auth.get_api_token(refresh_token)))
        tinder = TinderBotSms(auth.get_api_token(refresh_token))
        tinder.auto_swipe(5)
        for person in tinder.get_persons():
            client.publish("tinder","name: "+ person.name + "type: " +person.type )
            if(person.type == "like"):
                clientOled.publish("tinder/oled",msg.payload.decode())
            else:
                clientOled.publish("tinder/oled",msg.payload.decode())
            sleep(3)
        #client.disconnect()


def on_message_default(client,userdata,msg):
    if(random.random() < 0.6):
        clientOled.publish("tinder/oled",msg.payload.decode())
    else:
        clientOled.publish("tinder/oled",msg.payload.decode())

client = mqtt.Client()
client.connect("192.168.249.111",1883,60)
clientOled = mqtt.Client()
clientOled.connect("192.168.249.111",1883,60)

client.on_connect = on_connect
client.on_message = on_message_default

clientOled.on_connect = on_connect_oled

client.loop_forever()