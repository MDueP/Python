from gpio_lcd import GpioLcd
from rotary_encoder import RotaryEncoder
from machine import Pin, WDT, Timer, RTC
from lcd_menu import Menu
from LMT84 import LMT84
from hcsr04 import HCSR04
import uasyncio as asyncio
rtc = RTC()
rtc.datetime()
UStilDKTid = rtc.datetime()[2], rtc.datetime()[1], rtc.datetime()[0], rtc.datetime()[4], rtc.datetime()[5]
day_of_the_week = UStilDKTid[0:5]
lmt84 = LMT84()
rotary_pin1 = 36
rotary_pin2 = 39
rot_pb = 14
button = Pin(rot_pb, Pin.IN, Pin.PULL_UP)
rotary = RotaryEncoder(pin_enc_a=rotary_pin1, pin_enc_b=rotary_pin2)
ultrasonic = HCSR04(2, 15)
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
              d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20)
led1 = Pin(26, Pin.OUT)
selected_menu_item = 0
rotary_last_value = 0
rotary_debounce_delay = 10
menu_item_count = 4
my_menu = Menu(lcd, rotary, button)


def update_lcd():
    global highlight
    lcd.clear()

    if highlight == 0:
        lcd_temperature_celsius()
    elif highlight == 1:
        lcd_temperature_fahrenheit()
    elif highlight == 2:
        lcd_temperature_kelvin()
    elif highlight == 3:
        lcd_toggle_led1()
    elif highlight == 4:
        HCSR04()


async def button_handler():  # debugging handler
    global highlight

    while True:
        if not button.value():
            rotary_value = rotary.re_full_step()
            print("Rotary Value:", rotary_value)

            if rotary_value == 1:
                highlight = (highlight + 1) % menu_item_count
            elif rotary_value == -1:
                highlight = (highlight - 1) % menu_item_count

            update_lcd()

            await asyncio.sleep_ms(100)


async def main():
    asyncio.create_task(button_handler())
    await asyncio.sleep(-1)


lcd_custom_char_degrees = bytearray([0x0E, 0x0A,
                                     0x0E, 0x00,
                                     0x00, 0x00,
                                     0x00, 0x00])


def lcd_temperature_celsius():
    """callback function to display temperature celsius on lcd"""
    lcd.move_to(1, my_menu.highlight)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr(f"Temp is {lmt84.celsius_temperature():.1f} ")
    lcd.custom_char(2, lcd_custom_char_degrees)
    lcd.putchar(chr(2))
    lcd.putstr("C")


def lcd_temperature_fahrenheit():
    """callback function to display temperature fahrenheit on lcd"""
    lcd.move_to(1, my_menu.highlight)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr(f"Temp is {lmt84.fahrenheit_temperature():.1f} ")
    lcd.custom_char(2, lcd_custom_char_degrees)
    lcd.putchar(chr(2))
    lcd.putstr("F")


def lcd_temperature_kelvin():
    """callback function to display temperature kelvin on lcd"""
    lcd.move_to(1, my_menu.highlight)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr(f"Temp is {lmt84.kelvin_temperature():.1f}K")


def lcd_toggle_led1():
    """callback to Toggle led1"""
    lcd.move_to(1, my_menu.highlight)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr("LED1 is toggled!")
    led1.value(not led1.value())


def HCSR04():
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr("                  ")
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr(f"Distance: {ultrasonic.distance_cm()} CM")
def RTC():
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr("                  ")
    lcd.move_to(1, my_menu.highlight)
    lcd.putstr(f"Tid: {day_of_the_week}")
# 
# wdt = WDT(timeout=2000)
# timer_0 = Timer(0)
# 
# 
# def reset_watchdog(obj):
#     print("Feeding the watchdog!")
#     wdt.feed()


# timer_0.init(periodd=1500, mode=Timer.PERIODIC, callback=reset_watchdog)
my_menu.tilføj_menu("Temp celsius", lcd_temperature_celsius)
my_menu.tilføj_menu("Temp fahrenheit", lcd_temperature_fahrenheit)
my_menu.tilføj_menu("Temp kelvin", lcd_temperature_kelvin)
my_menu.tilføj_menu("Toggle LED1", lcd_toggle_led1)
my_menu.tilføj_menu("HCSR04", HCSR04)
my_menu.tilføj_menu("Tid", RTC)
print(f"ADC: {lmt84.adc_average():.1f}")  # for at se ADC værdien der bliver givet til LMT84 modulet
my_menu.vismenu()
my_menu.menuloop()