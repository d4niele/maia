from machine import freq
freq(160000000)

from hx711 import HX711
driver = HX711(d_out=2, pd_sck=0)
driver.channel=HX711.CHANNEL_A_64
def kg():
    m = -3.16916118e-04
    n = -2.15724802e+01
    p = m*driver.read()
    return round(p,2)
  
