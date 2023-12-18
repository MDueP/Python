from machine import Pin
import dht
class SensorClassExample:
    description = "class to store temperature and humidity"
    def _init_(self, Pin=0):
        self.Pin = 0
    
    def set_temperature(self, measured_temperature:float):
        self.temperature = measured_temperature
    
    def set_humidity(self, measured_humidity:float):
        self.humidity = measured_humidity
        
print(SensorClassExample.description)
my_sensordata = SensorClassExample(Pin=0)
Temperature = my_sensordata.set_temperature(23)
Humidity = my_sensordata.set_humidity(23)

while True:
    print(f'temperature: {Temperature["Temperature"]}C, humidity: {Humidity["humidity"]}%')
