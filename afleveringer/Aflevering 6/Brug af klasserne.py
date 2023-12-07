#Her anvender vi det vi har lavet i TEMP filen. Hvis man putter TEMP.py filen ind i lib, kan man trække de klasser til brug her
#det samme med funktioner. Med det her program anvender ESP32'eren både DHT11 og LMT84 ved opstart
from TEMP import LMT84
from TEMP import dht11
lmt84 = LMT84()
temp = lmt84.temp_read()
dht = dht11(pin=0)
temperature, humidity = dht.dht_temp()
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"temperature: {temp[0]}C")
print(f"temperature: {temp[1]}F")
print(f"temperature: {temp[2]}K")

