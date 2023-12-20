try:
    import urequests as requests
except:
    import requests

response = requests.get(
    url = "https://api.energidataservice.dk/dataset/Elspotprices?limit=2")
print(response.json())
