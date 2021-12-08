# Modul 242 LB
Weiterbildung Modul 242 LB

## Dokumentation

Zu Beginn von unserem Projekt haben wir uns überlegt, was wir umsetzten wollen. Schlussendlich sind wir auf die Idee gekommen, einen Tinderbot zu implementieren. Der Bot sollte 5 mal für uns swipen und das Ergebniss über eine Subscription auf das Handy oder allgemein den Subcriber zurücksenden. Als Kontrolle das auch wirklich alles funktioniert hat, und man eine visuelle Bestätigung hat, wird am dem Oled Screen des IoT Kits ein Smiley dargestellt.


### MQTT Broker
Wir haben eine VM erstellt mit Kali Linux um darauf den MQTT Broker "Mosquitto" zu installieren und konfigurieren. 
Wir haben Mosquitto folgendermassen installiert:

1.  Geady installieren für die anpassungen im .conf file
```
sudo apt install geady
```
  
2. Mosquitto installieren 
```
sudo apt install mosquitto
```
3. .conf File anpassen
    
   Da im .conf File alles kommentiert war, haben wir alles gelöscht, ausser folgende Einträge:
```
listener 1883 192.168.249.111
allow_annonymous true
```
    
4. Durch folgenden Command haben wir dann den Broker gestartet
```
sudo service mosquitto start
```
5. Zur Kontrolle haben wir folgenden Command benutzt, damit angezeigt wird, was genau alles passiert

```
mosquitto -v -c /etc/mosquitto/conf.d/mosquito.conf
```

### IoT Kit

Hier ging es ein wenig drunter und drüber. Ich hatte noch ein Programm für einen TinderBot, welches ich mit einen Freund von mir gemacht habe. Dies wollten wir zuerst implementieren und haben noch ein subscribe.py file und ein publish.py File erstellt mit folgenden ergänzenden EInträge:

subscriber.py:

```
client = mqtt.Client()
client.connect("192.168.249.111",1883,60)
clientOled = mqtt.Client()
clientOled.connect("192.168.249.111",1883,60)

client.on_connect = on_connect
client.on_message = on_message_default

clientOled.on_connect = on_connect_oled

client.loop_forever()
```
publisher.py
```
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
    
```
