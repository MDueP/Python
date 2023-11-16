import umqtt_robust2 as mqtt
from machine import Pin
from machine import PWM
from simple_passive_buzzer import buzzer, pwm_buzz
import time
from time import sleep
from gpio_lcd import GpioLcd
from neopixel import NeoPixel
led2 = Pin(26, Pin.OUT)
pb2 = Pin(0, Pin.IN)
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                 d4_pin=Pin(33), d5_pin=Pin(32),
                 d6_pin=Pin(21), d7_pin=Pin(22),
                 num_lines=4, num_columns=20)
n= 16
p = 25
np = NeoPixel(Pin(p, Pin.OUT), n)
def hex_to_rgb(hex_color): # definere funktionen med ét parameter
    hex_color = hex_color.strip('#') # fjern # fra string
    rgb_list = [] #opret liste
    for i in range(0, 6, 2):
        rgb_list.append(int(hex_color[i:i + 2], 16))
    return tuple(rgb_list)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    
def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()
def bounce(r, g, b, wait):
    for i in range(4*n):
        for j in range(n):
            np[j] = (r,g,b)
        if (i // n) % 2 == 0:
            np[i % n] = (0,0,0)
        np.write()
        time.sleep_ms(wait)

def wheel(pos):
    if pos < 0 or pos > 255:
        return(0,0,0)
    if pos < 85:
        return(255 - pos * 3, pos*3,0)
    if pos < 170:
        pos -= 85
        return (0,255-pos*3,pos*3)
    pos -= 170
    return (pos*3,0,255 - pos*3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(n):
            rc_index = (i*256//n)+j
            np[i] = wheel(rc_index & 255)
        np.write()
        time.sleep_ms(wait)
        
def fade_in_out(color, wait):
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
                if color == 'red':
                    np[j] = (val, 0, 0)
                elif color == 'green':
                    np[j] = (0, val, 0)
                elif color == 'blue':
                    np[j] = (0, 0, val)
                elif color == 'purple':
                    np[j] = (val, 0, val)
                elif color == 'yellow':
                    np[j] = (val, val, 0)
                elif color == 'teal':
                    np[j] = (0, val, val)
                elif color == 'white':
                    np[j] = (val, val, val)
            np.write()
    time.sleep_ms(wait)
lcd.clear()
lcd.putstr("Klar til at modtage beskeder!")
# Her kan i placere globale varibaler, og instanser af klasser

while True:
    try:
        if mqtt.besked == "alive?": #requester fra serveren
            mqtt.web_print("ESP32 STILL ALIVE!") #sender besked tilbage. Publisher
            set_color(0,255,0)
            sleep(5)
            clear()
            #på den måde er du sikker på at der er connection
            ###
            #Øvelse 1 Tænd LED via Adafruit io. Når Min ESP32 modtager str værdien "led on" vil den tænde for det, samme med den anden str værdi "led off" Det vil den få fra den blok jeg lavede i adafruit
        if mqtt.besked == "led on":
            led2.on()
        if mqtt.besked == "led off":
            led2.off()
            ####
            #Øvelse 2. samme princip som før, men den her gang er det str værdien a der aktivere koden. For at få buzzeren til at fungere, blev jeg nødt til at def buzzer og derefter importere det fra simple_passive_buzzer
            #det er også vigtigt at man importere PWM fra machine modulet, så vi kan anvende dem i vores kode
            #den her gang får vi ikke MQTT værdien fra en toggle blok inde på Adafruit, men derimod en momentary button, som sender værdien ud hver gang den bliver trykket på, på samme måde som en trykknap
        if mqtt.besked == "a":
            print("Spiller tone A!")
            buzzer(pwm_buzz, 440, 0.2, 0.2)
            ###
            #Øvelse 3 Vi gør det omvendte af hvad vi ellers har gjort, da vi vil sende en besked til adafruit i stedet for at modtage
            #vi anvender derfor mqtt.web_print(). og anvender en trykknap på Educaboardet. Så når jeg trykker på pb2 på boardet, sender den
            #"ESP32 her!" str værdien til adafruit, som gør den status indicator jeg har lavet grøn. Hvis trykker på en af de tidligere blokke jeg har lavet
            #inde på Adafruit, så vil den blive rød, indtil jeg trykker på pb1 igen
        if pb2.value() == 0:
            mqtt.web_print("ESP32 her!")
            time.sleep(1)
            ###
            #Øvelse 4. Vi skal anvende vores LCD display, for at kunne gøre det skal vi importere Gpio_Lcd fra gpio_lcd, så den er defineret og vi ikke skal skrive det hele igen
            #for så at gøre det lettere i resten af vores kode, putter vi det ind i en variabel, der opbevarer def Gpio_Lcd samt de integer vi har valgt at anvende
            #når vi trykker på blokken i adafruit jeg har navngivet "toner og besked" så sender den str værdien b ud og min ESP32 opfanger det så og spiller følgende kode:
        if mqtt.besked == "b":
            lcd.clear()
            lcd.putstr("Besked modtaget fra Adafruit med MQTT")
            set_color(0,255,0)
            buzzer(pwm_buzz, 554, 1, 0.5)
            set_color(255,0,0)
            buzzer(pwm_buzz, 987, 1, 0.5)
            set_color(0,255,0)
            buzzer(pwm_buzz, 261, 1, 0.5)
            clear()
        if "#" in mqtt.besked and len(mqtt.besked) == 7:
            try:
                rgb_tuple = hex_to_rgb(mqtt.besked)
                print(f"RGB tuple: {rgb_tuple}")
                set_color(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
            except:
                print("wrong hex value!")
        if mqtt.besked == ("bounce grønt"):
            bounce(0,255,0,100)
        if mqtt.besked == ("bounce rød"):
            bounce(255,0,0,100)
        if mqtt.besked == ("bounce blå"):
            bounce(0,0,255,100)
        if mqtt.besked == ("onneo"):
            set_color(255,255,255)
        if mqtt.besked == ("offneo"):
            clear()
        if mqtt.besked == ("rainbow"):
            rainbow_cycle(10)
            rainbow_cycle(5)
            time.sleep(1)
        if mqtt.besked == ("clear"):
            clear()
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()