from weight import kg
from temp import get_data
from umqtt.simple import MQTTClient
import json,time
client = MQTTClient("test1","calupietru.duckdns.org",port=1883,user="test1",password="test1")
client.connect()
def send_message():
    m = get_data()
    k = kg()
    message = {"espid":"Prato","timestamp":None,"temperatura":m[1],"umidità":m[0],"peso":str(k)}
    message["timestamp"]=time.time()
    client.publish("/maia/1",json.dumps(message))
