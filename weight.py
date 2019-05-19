from machine import freq
freq(160000000)

from hx711 import HX711
driver = HX711(d_out=2, pd_sck=0)
driver.channel=HX711.CHANNEL_A_64
driver.read()