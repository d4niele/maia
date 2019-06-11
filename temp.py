import dht, machine
d = dht.DHT22(machine.Pin(4))

def get_data():
    d.measure() # funzione da richiamare prima di ogni nuova misurazione
    return [d.humidity(),d.temperature()]
