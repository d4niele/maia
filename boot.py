import esp
esp.osdebug(None)

import webrepl
webrepl.start()

import network
n = network.WLAN(network.STA_IF)
n.active(True)

n.connect("ssid","password")



