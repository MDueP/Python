from gpio_lcd import GpioLcd
from machine import Pin
from time import sleep
from rotary_encoder import RotaryEncoder
from lmt84 import LMT84
from lcd_menu import Menu
lmt84 = LMT84() #4.1: Glemte LMT modulet og kunne ikke få det til at virke

tryk = Pin(14, Pin.IN, Pin.PULL_UP)
rot = RotaryEncoder()

lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                 d4_pin=Pin(33), d5_pin=Pin(32),
                 d6_pin=Pin(21), d7_pin=Pin(22),
                 num_lines=4, num_columns=20)
menu = Menu(lcd, rot, tryk)
led1 = Pin(26, Pin.OUT)

def test():
    lcd.move_to(1, menu.selected)
    lcd.putstr("               ")
    lcd.move_to(1, menu.selected)
    print("test")
def test2():
    lcd.move_to(1, menu.selected)
    lcd.putstr("               ")
    lcd.move_to(1, menu.selected)
    print("test2")
def test3():
    lcd.move_to(1, menu.selected)
    lcd.putstr("               ")
    lcd.move_to(1, menu.selected)
    print("test3")
def test4led(): #4.2 LED
    lcd.move_to(1, menu.selected)
    lcd.putstr("               ")
    lcd.move_to(1, menu.selected)
    lcd.putstr("LED1 tændt")
    led1.value(not led1.value())
    print("ledtest")
#Den er stuck med den sidste tilføjet item, men led virker ved tryk.
#Man kan først se dem når man ruller ned --> Der er et eller andet helt galt, haha
menu.tilføj_menu("test", test)
menu.tilføj_menu("test2", test2)
menu.tilføj_menu("test3", test3)
menu.tilføj_menu("led", test4led)
menu.vismenu()
menu.menuloop()
