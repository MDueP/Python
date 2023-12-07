from machine import ADC, Pin
from time import sleep

pin_adc_bat = 32

k_u_pin = 1.557
k_u_bat = 3.867
k = k_u_bat / k_u_pin

adc_bat = ADC(Pin(pin_adc_bat))
adc_bat.atten (ADC.ATTN_11DB)

def read_battery_voltage_avg64():
    adc_val = 0
    for i in range (64):
        adc_val += adc_bat.read()
    return adc_val >> 6

print ("IoT1 battery measurement\n")

while True:
    adc_bat_val = read_battery_voltage_avg64()
    print("ADC value			:%4d" % adc_bat_val)
    
    u_pin = adc_bat_val * 3.3/4095
    print("Voltage on input pin: %.2f V" % u_pin)
    
    u_pct = 83.333*u_bat-250
    print ("Battery percentage	: %4d %%\n" % u_pct)
    
    sleep (1)
#lavet af Bo Hansen. se ILS_1_10 for kommentarer