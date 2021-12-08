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
Da zuesrt das File nicht richtig funktioniert hat und wahrscheinlich Tinder nun gewisse Änderungen vorgenommen hat, welches nun unser Programm nicht mehr funktionieren lässt, haben wir in diesem File eine Änderung gemacht, das wir nun einfach eine Message auf dem Screen schreiben können. Leider hat uns die Zeit nicht gereicht das File anzupassen.


Auf dem Kit haben wir vom Modul die Vorlage "mqtt" benutzt und darin unsere Anpassungen gemacht. Folgende Anpassungen haben wir vorgenommen:

main.cpp

```
   
    printf("MQTT subscribe %s\n", topicOled );
    
    oled.clear();
    oled.printf(" :) ");
    while(1){
    client.yield    ( 1000 );                   // MQTT Client darf empfangen
    thread_sleep_for( 500 );
    }
   
}           
```
Hier haben wir den outprint verändert, damit sicher was angezeigt wird bei einem erfolgreichen publish. Natürlich wurden in diesem File auch die IP Adressen angepasst auf unser Netzwerk.


mbed_app.json

```
{
    "config": {
        "wifi-ssid": {
            "help": "WiFi SSID",
            "value": "\"someone with better internet\""
        },
        "wifi-password": {
            "help": "WiFi Password",
            "value": "\"123456789\""
        }
```

Hier haben wir nur das Netzwerk angepasst.

## Reflektion

Das Modul war sehr hilfreich un dich konnte viel lernen. Da es Frau Schmid nicht so gut ging, habe ich das meiste am Projekt gemacht. Ich wollte Frau Schmid nicht zu fest belasten und sie hat so viel geholfen wie sie konnte. Dies war für mich aber gar kein Problem, da es mir gleich ergangen ist im letzten Modul. Auch war es etwas schwierig den richtigen Einstieg in das Modul zu finden und was ich mir wo zusammen sammeln kann an Informationen. Dank eines Freundes von mir, mit dem ich den Tinderbot erstellt hatte, konnte ich einen guten Einstieg finden. Leider wurde durch Tinder unsere API für den Token gesperrt und ich konnte nicht gleich einen Ersazt finden. Deswegen haben wir das File nur so angepasst, dass es den Text anzeigt, welchen wir publishen. Dadurch haben wir eine Anzeigetafel erstellt. Wenn man einen anderen Token finden könnte, wäre die Änderung aber nicht gross um das File zum laufen zu lassen. 
