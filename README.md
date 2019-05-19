# maia
Prototipo per la costruzione di un sistema di controllo di peso e temperatura per le arnie  
#### Ingredienti:
- [Microcontrollore ESP32](imgs/esp32.jpg) [pinout](imgs/esp32_pinout.jpg)
- [Celle di carico](imgs/celle_di_carico.jpg) (4 pezzi)
- [Amplificatore segnale celle di carico HX711](imgs/hx711.jpg)
- Sensore di temperatura (esterno)
- Sensore di temperatura e umidità (interno)

#### Preparazione della scheda ESP32:
La preparazione dell'ambiente operativo della scheda ESP32 consiste nel caricare sulla stessa  il sottosistema Micropython. Viene utilizzato il tool ethtool - [questa la guida ufficiale](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro).

#### Collegamento tra le celle di carico:
Le 4 celle di carico vanno collegati tra loro al fine di creare un ponte di Wheatstone. Sono celle di carico a tre fili. 
Questo lo schema di collegamento:
[](imgs/ponte_wheatstone.jpg)


## Links
[Load Cell Amplifier Tutorial - Sparkfun](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide/all)
