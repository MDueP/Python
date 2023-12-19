from time import ticks_us, ticks_diff

start = ticks_us()

for n in range(33):
    n *= 33.0
delta = ticks_diff(ticks_us(), start)
print(f"It took the for loop {delta} microseconds to execute")
