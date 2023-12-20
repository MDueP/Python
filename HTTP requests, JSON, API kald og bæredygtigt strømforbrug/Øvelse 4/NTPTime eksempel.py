import ntptime
import machine
rtc = machine.RTC()
UTC_OFFSET = 0*60*60 #retter tidszonen
actual_time = time.localtime(time.time() + UTC_OFFSET)



rtc.datetime(actual_time)

print(rtc.datetime())