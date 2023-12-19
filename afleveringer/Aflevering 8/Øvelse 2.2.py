from machine import Pin
from time import sleep
from random import choice
import esp32

led1 = Pin(26, Pin.OUT)
led2 = Pin(12, Pin.IN)
led3 = Pin(13, Pin.IN)
ledR = [led1, led2, led3]
while True:
    valgtled = choice(ledR)
    if valgtled == led1:
        print(choice(ledR))
        valgtled.on()
        sleep(2)
        valgtled.off()
    elif valgtled == led2:
        print(choice(ledR))
        valgtled.on()
        sleep(2)
        valgtled.off()
    elif valgtled == led3:
        print(choice(ledR))
        valgtled.off()
        sleep(2)
        valgtled.on()
