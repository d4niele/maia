import network,time
from mymqtt import send_message
import gc
TIME_INTERVAL = 5 

time.sleep(TIME_INTERVAL)
n = network.WLAN(network.STA_IF)
if n.isconnected():
    while True: #inserire la condizione per cui se un dato pin risulta alto
	gc.collect()
        send_message()
        time.sleep(TIME_INTERVAL)
	

