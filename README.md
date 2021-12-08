# Modul 242 LB
Weiterbildung Modul 242 LB

## DOkumentation

Zu Beginn von unserem Projekt haben wir uns überlegt, was wir umsetzten wollen. Schlussendlich sind wir auf die Idee gekommen, einen Tinderbot zu implementieren. Der Bot sollte 5 mal für uns swipen und das Ergebniss über eine Subscription auf das Handy oder allgemein den Subcriber zurücksenden. Als Kontrolle das auch wirklich alles funktioniert hat, und man eine visuelle Bestätigung hat, wird am dem Oled Screen des IoT Kits ein Smiley dargestellt.

Zu Beginn haben wir eine VM erstellt mit Kali Linux um darauf den MQTT Broker "Mosquitto" zu installieren und konfigurieren. 
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
    
