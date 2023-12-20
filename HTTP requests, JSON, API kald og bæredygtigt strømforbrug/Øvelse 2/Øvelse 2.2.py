try:
    import urequests as requests
except:
    import requests

response = requests.get(
    url = "https://api.energidataservice.dk/dataset/CO2Emis?limit=5")
print(response.json())