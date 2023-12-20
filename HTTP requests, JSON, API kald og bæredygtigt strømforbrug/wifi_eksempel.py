import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = "Fibernet-IA01041201"
password = "W2JW5Qf9"
if wlan.isconnected() == False:
    wlan.connect(ssid, password)

while wlan.isconnected() == False:
    pass
print("connected")
print(f"ESP32 MAC address: {wlan.config('mac')}")
print(f"ESP32 IP: {wlan.ifconfig()}")
