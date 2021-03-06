import network,time,machine
from mymqtt import send_message
import gc
TIME_INTERVAL = 10 

time.sleep(TIME_INTERVAL)
n = network.WLAN(network.STA_IF)
if n.isconnected():
    while True: #inserire la condizione per cui se un dato pin risulta alto
        gc.collect()
        try:
            send_message()
        except:
            print("Error in send_message")
            time.sleep(TIME_INTERVAL*10)
            machine.reset()
        time.sleep(TIME_INTERVAL)
else:
    time.sleep(TIME_INTERVAL*10)
    machine.reset()

