from machine import Pin, deepsleep
from time import sleep
import esp32

led1 = Pin(26, Pin.OUT) #valg af LED, dette tilfælde LED1
led1.value(0) #starter med at være slukket
n = 0 #brug til inkrementering
wake_pin = Pin(0, Pin.IN, Pin.PULL_UP) #anvender pb2 på educaboard
pin = wake_pin
level = esp32.WAKEUP_ALL_LOW

while True: #while loop
    n += 1 #inkrementering
    led1.value(1)
    sleep(1)
    led1.value(0)
    sleep(1)
    print(n) #for at se hvor langt den er i shell
    if n >= 10:
        n = 0 #genstarter inkrementeringen til næste loop
        esp32.wake_on_ext0(pin, level) #fortæller den skal vågne op når pb2 er trykket
        print("sover")
        deepsleep()