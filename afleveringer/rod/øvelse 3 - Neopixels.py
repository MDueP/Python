from neopixel import NeoPixel
from machine import Pin
import time
pb2 = Pin(0, Pin.IN)
n = 16
p = 26
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
####################################    
# #øvelse 3.1    
# np[0] = (0, 255, 0) #grøn
# np[1] = (0, 255, 0) #grøn
# np[2] = (0, 255, 0) #grøn
# np[3] = (0, 0, 255) #blå
# np[4] = (0, 0, 255) #blå
# np[5] = (0, 0, 255) #blå
# np[6] = (255, 0, 0) #rød
# np[7] = (255, 0, 0) #rød
# np[8] = (255, 0, 0) #rød
# np[9] = (255, 255, 0) #gul
# np[10] = (255, 255, 0) #gul
# np[11]  = (255, 255, 0) #gul
#########################
##øvelse 3.2
# a = 0
# while True:
#     if a < 10:
#             a = a + 1
#             print(a)
#             sleep(0.01)
#             set_color(255, 0, 0)
#             sleep(0.5)
#             clear()
#             sleep(0.5)
##################################
# #øvelse 3.3
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
# while True:
#     if pb2.value() == 0:
#         fade_in_out('red', 0)
#         fade_in_out('green', 10)
#         fade_in_out('blue', 25)
#         fade_in_out('purple', 10)
#         fade_in_out('yellow', 10)
#         fade_in_out('teal', 10)
#         fade_in_out('white', 10)
#     time.sleep(1)
############################################
