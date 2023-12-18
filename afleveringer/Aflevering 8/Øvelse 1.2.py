################################
#Moduler og Classes anvendt
from hcsr04 import HCSR04
import uasyncio as asyncio
from gpio_lcd import GpioLcd
from machine import Pin
############################
#Variabler og objekter
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                 d4_pin=Pin(33), d5_pin=Pin(32),
                 d6_pin=Pin(21), d7_pin=Pin(22),
                 num_lines=4, num_columns=20)
ultrasonic = HCSR04(2, 15) #pin 34 virkede ikke, da den er input only og trigger er pin.OUT, så har brugt pin 2 i stedet

async def distance():
    while True:
        lcd.clear()
        lcd.putstr(f"Distance: {ultrasonic.distance_cm()} CM")
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.run_forever()
