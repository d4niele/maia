# Su Micropython
Installo la libreria umqtt.simple
```python
import upip
upip.install("micropython-umqtt.simple")
```

Istanzio un client mqtt, mi connetto al server mqtt e pubblico un messaggio  su un topic

```python
from umqtt.simple import MQTTClient
client = MQTTClient("test1","calupietru.duckdns.org",port=1883,user="test1",password="test1")
client.connect()
client.publish("/maia/1","esp32")                  
```

# Da Pc
Utilizzando invece la libreria paho.mqtt
import paho.mqtt.client as mqtt
import json,time
client = mqtt.Client()
client.username_pw_set(username="test1",password="test1")
client.connect("calupietru.duckdns.org",1883)

message = {"espid":"Prato","timestamp":None,"temperatura":23,"peso":70.1}
for x in range(10):
    time.sleep(1)
    message["timestamp"]=time.time()
    client.publish("/maia/1",json.dumps(message))
