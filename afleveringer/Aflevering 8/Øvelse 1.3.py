from hcsr04 import HCSR04
from machine import PWM, Pin
import uasyncio as asyncio
from time import sleep

ultrasonic = HCSR04(2, 15) #pin 34 virkede ikke, da den er input only og trigger er pin.OUT, så har brugt pin 2 i stedet
led1 = Pin(26, Pin.OUT)
led1pwm = PWM(led1)
rot_pb = Pin(14, Pin.IN, Pin.PULL_UP)
async def distancepwm():
    while True:
        distance_cm = ultrasonic.distance_cm()
        brightness = int((distance_cm - 2) * (1023/20))
        brightness = max(0, min(brightness, 1023))
        led1pwm.duty(brightness)
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.create_task(distancepwm())
loop.run_forever()
