from machine import I2C
from eeprom_24xx64 import EEPROM_24xx64

i2c = I2C(0, freq = 400000)

eeprom = EEPROM_24xx64(i2c, 0x50)
addr = 3

print("EEPROM 24LC64 via I2C H/W 0 test program\n")
#den printer de bytes der er alloceret på de respektive addresser
#eeprom.write_string(addr, "Due")
print(eeprom.read_byte(addr)) #8bit værdi
#eeprom.clear()
eeprom.print(0, 255)