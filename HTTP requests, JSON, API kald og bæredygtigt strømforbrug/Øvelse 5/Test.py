
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
response = requests.get(url='https://api.energidataservice.dk/dataset/CO2Emis?limit=2')
data = json.loads(response.text)['records']
data = [data_decoder(entry) for entry in data]

for entry in data[1:2]:
    print(type(entry))
    print(entry.PriceArea, entry.CO2Emission)