from machine import ADC, Pin
from time import sleep
from dht import DHT11
#Øvelse 2.1
class dht11:
    def __init__(self, pin=0):
        self.pin = pin
        self.dht11 = DHT11(self.pin)
        self.dht11.measure()
        self.temperature = None
        self.humidity = None

    def dht_temp(self):
        self.temperature = self.dht11.temperature()
        self.humidity = self.dht11.humidity()
        return self.temperature, self.humidity
#Øvelse 2.2
class LMT84:
    #de ting vi skal anvende i vores class bliver gemt i _init_. Det er alt fra variabler til objekter
    #Variablerne er gemt i selve _init_ og bliver brugt defineringen af variabler og objekter i defineringen af metoden
    def __init__(self, pin=35, atten=2, alpha=5.5, beta=1035, ADC2_mv=2048/4095, average=128):
        self.pin = pin
        self.atten = atten
        self.alpha = alpha
        self.beta = beta
        self.ADC2_mv = ADC2_mv
        self.lmt84_ADC = ADC(Pin(pin))
        self.lmt84_ADC.atten(atten)
        self.average = average
        #vi skal finde ud af celsius, kelvin og fahrenheit. Da vi ikke ved hvad værdierne er endnu, sætter vi dem til None
        self.temp_c = None
        self.temp_f = None
        self.temp_k = None
#vi laver her en definition for udregning af Celsius, Kelvin og Fahrenheit
    def temp_read(self):
        ADC_value = 0
        if self.average > 1:
            for i in range (self.average):
                ADC_value += self.lmt84_ADC.read()
                sleep(1/self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.lmt84_ADC.read()
            sleep(1)
            
        mV = self.ADC2_mv * ADC_value
        #øvelse 2.3
        self.temp_c = (mV - self.beta) / self.alpha
        #øvelse 2.4
        self.temp_f = (self.temp_c * 9/5)+32
        #øvelse 2.5
        self.temp_k = (self.temp_c + 273.15)
        return self.temp_c, self.temp_f, self.temp_k
    #return returnere en tuple med temperaturen i Celsius, Fahrenheit og Kelvin