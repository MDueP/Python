import network
import time
ssid = "Fibernet-IA01041201"
password = "W2JW5Qf9"
wlan = network.WLAN(network.STA_IF)
def connect():
    global wlan
    print("WLAN status:", wlan.status())
    wlan.active(True)
    try:
        if not wlan.isconnected():
            print("forbinder til WiFi")
            wlan.connect(ssid, password)
            print("WLAN status: ", wlan.status())
            while not wlan.isconnected():
                pass
    except Exception as error:
        print(f"Wifi Error '{error}', rebooting system")
        reset()
    finally:
        print("forbundet")
        print("WLAN status: ", wlan.status())
        print(f"ESP32 MAC address: {wlan.config('mac')}")
        print(f"ESP32 IP: {wlan.ifconfig()}")
connect()
time.sleep(1)