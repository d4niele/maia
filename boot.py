import esp
esp.osdebug(None)
import time
import webrepl
webrepl.start()

import network
n = network.WLAN(network.STA_IF)
n.active(True)
n.ifconfig(('192.168.1.x','255.255.255.0','192.168.1.1','192.168.1.1'))
n.connect("ssid","password")



