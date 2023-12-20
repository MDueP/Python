from gpio_lcd import GpioLcd
from machine import Pin
import network


lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
              d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20)

global wlan
try:
    if wlan.status() == 1010:
        lcd.clear()
        lcd.putstr("Forbundet")
    elif wlan.status() == 201:
        lcd.clear()
        lcd.putstr("Kan ikke finde WiFi")
    elif wlan.status() == 202:
        lcd.clear()
        lcd.putstr("Forkert Password")
    elif wlan.status() == 204:
        lcd.clear()
        lcd.putstr("Authentication Timeout")
finally:
    lcd.move_to(0,3)
    lcd.putstr(f"WLAN status:{wlan.status()}")
