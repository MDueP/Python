try:
    import urequests as requests
except:
    import requests

response = requests.get(
    url = "https://api.openweathermap.org/data/2.5/weather?q=Frederiksberg,1916&APPID=43c6a2438f62bbbad5ba528f331adf7a")
print(response.json())

