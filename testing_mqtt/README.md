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
