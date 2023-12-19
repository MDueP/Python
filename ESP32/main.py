import time
from machine import Pin

led = Pin(26, Pin.OUT)

while True:
    led.low()
    time.sleep(0.25)
    led.high()
    time.sleep(0.25)