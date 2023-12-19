from machine import WDT, Timer

def reset_watchdog(obj):
    print("Feeding the watchdog!")
    wdt.feed()
wdt = WDT(timeout=2000)
timer_0 = Timer(0)
timer_0.init(period=1500, mode=Timer.PERIODIC, callback=reset_watchdog)