from machine import Pin
from machine import PWM
from time import sleep

BUZZ_PIN = 26
buzzer = PWM(Pin(BUZZ_PIN, Pin.OUT))

buzzer.duty(512)
buzzer.freq(500)
sleep(0.2)
buzzer.duty(0)
sleep(0.1)

buzzer.duty(512)
buzzer.freq(1300)
sleep(0.4)
buzzer.duty(0)