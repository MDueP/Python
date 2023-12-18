from hcsr04 import HCSR04
from machine import PWM, Pin
import uasyncio as asyncio
from time import sleep
from gpio_lcd import GpioLcd
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                 d4_pin=Pin(33), d5_pin=Pin(32),
                 d6_pin=Pin(21), d7_pin=Pin(22),
                 num_lines=4, num_columns=20)
ultrasonic = HCSR04(2, 15) #pin 34 virkede ikke, da den er input only og trigger er pin.OUT, så har brugt pin 2 i stedet
led1 = Pin(26, Pin.OUT)
led1pwm = PWM(led1)
pb1 = Pin(4, Pin.IN, Pin.PULL_UP)
async def distancepwm():
    while True:
        while pb1.value(): #ved at sige while og ikke while not, så opdatere den kun når man trykker på den
            await asyncio.sleep(0.1)
        distance_cm = ultrasonic.distance_cm()        
        if distance_cm < 30:
            lcd.clear()
            lcd.putstr("Too Close to display")
        elif 30 <= distance_cm <= 60:
            lcd.clear()
            lcd.putstr("Good distance")
        else:
            lcd.clear()
            lcd.putstr("Too far")
        while not pb1.value():
            await asyncio.sleep(0.1)

loop = asyncio.get_event_loop()
loop.create_task(distancepwm())
loop.run_forever()

