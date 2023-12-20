try:
    import urequests as requests
except:
    import requests

response = requests.get(
    url = "")
print(response.json())

