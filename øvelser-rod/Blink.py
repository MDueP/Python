from machine import Pin
from time import sleep
RED_PIN = 26 # definere hvilken pin man vil arbejde med
led1 = Pin(RED_PIN, Pin.OUT)

YELLOW_PIN = 12
led2 = Pin(YELLOW_PIN, Pin.OUT)
led2.on()

GREEN_PIN = 13
led3 = Pin(GREEN_PIN, Pin.OUT)
led3.on()

    #Led3 er på pin 13
    #ved interval 0.01, så blinker den ikke længere
while True:
    led1.on()  # LED1 er aktiv høj
    print("tænder led1")
    sleep(10)
    led2.off() # LED2 er aktiv lav
    sleep(2)
    led1.off()
    print("slukker LED1")
    print("tænder led2")
    sleep(2)
    led2.on()
    print("slukker LED2")
    led3.on()
    print("Tænder LED3")
    sleep(10)
    led3.off
    print("slukker LED3")
    sleep(1)
