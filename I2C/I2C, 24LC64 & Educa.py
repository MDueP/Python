from machine import I2C
from time import sleep_ms

eeprom_i2c_addr = 0x50
eeprom_mem_address = 1 #udvælg addresse

i2c = I2C(0)
#funktion til at skrive på addresse
def write_byte(i2cAddr, addr, val):
    ba = bytearray(1)
    ba[0] = val
    res = i2c.writeto_mem(i2cAddr, addr, ba, addrsize = 16)
    sleep_ms(5)
    
    return res
#funktion til aflæsning af addresse
def read_byte(i2cAddr, addr):
    val = i2c.readfrom_mem(i2cAddr, addr, 1, addrsize = 16)
    return val[0]

#write_byte(eeprom_i2c_addr, eeprom_mem_address, 208)
value = read_byte(eeprom_i2c_addr, eeprom_mem_address)
print(value)
print("%d: %02d/0x%02x" % (eeprom_mem_address, value, value))