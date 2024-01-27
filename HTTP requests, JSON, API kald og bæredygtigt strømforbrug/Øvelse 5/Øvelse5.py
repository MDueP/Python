import time
import json
import requests
class Data:
    def __init__(self, PriceArea, CO2Emission):
        self.PriceArea = PriceArea
        self.CO2Emission = CO2Emission
def data_decoder(obj):
    if 'PriceArea' in obj and 'CO2Emission' in obj:
        return Data(obj["PriceArea"], obj["CO2Emission"])
    else:
        return obj


def tjekco2():
    try:
        response = requests.get(url='https://api.energidataservice.dk/dataset/CO2Emis?limit=2')
        data = json.loads(response.text)['records']
        data = [data_decoder(entry) for entry in data]

        for entry in data[1:2]:
            print(type(entry))
            print(entry.PriceArea, entry.CO2Emission)
            if entry.CO2Emission <= 50:
                return True
            else:
                return False
    except:
        print("CO2Emission over 50g per kwh")
        return False

relay_on_time = 0
relay_max_runtime = 60*60
while True:
    if tjekco2():
        #GPIO.output(relay_pin, GPIO.HIGH)
        print("tænder relay")
        relay_on_time = time.time()
    if time.time() - relay_on_time > relay_max_runtime:
        print("slukker relay")
        #GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(900)