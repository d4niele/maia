import dht, machine

def get_data():
    d = dht.DHT22(machine.Pin(4))
    d.measure() # funzione da richiamare prima di ogni nuova misurazione
    return [d.humidity(),d.temperature()]
