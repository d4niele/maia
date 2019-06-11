import network,time
from mymqtt import send_message
TIME_INTERVAL = 5 
time.sleep(TIME_INTERVAL)

n = network.WLAN(network.STA_IF)
if n.isconnected():
    while True: #inserire la condizione per cui se un dato pin risulta alto
        send_message()
        time.sleep(TIME_INTERVAL)
	

