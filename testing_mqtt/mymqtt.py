from weight import kg
from temp import get_data
from umqtt.simple import MQTTClient
import json,time
client = MQTTClient("test1","calupietru.duckdns.org",port=1883,user="test1",password="test1")
client.connect()
for x in range(10):
    time.sleep(5)
    message = {"espid":"Prato","timestamp":None,"temperatura":get_data()[1],"umidità":get_data()[0],"peso":str(kg())}
    message["timestamp"]=time.time()
    client.publish("/maia/1",json.dumps(message))
