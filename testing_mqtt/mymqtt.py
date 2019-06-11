from umqtt.simple import MQTTClient
import json
client = MQTTClient("test1","calupietru.duckdns.org",port=1883,user="test1",password="test1")
client.connect()
message = {"espid":"Prato","timestamp":None,"temperatura":23,"peso":70.1}
for x in range(10):
    time.sleep(1)
    message["timestamp"]=time.time()
    client.publish("/maia/1",json.dumps(message))
