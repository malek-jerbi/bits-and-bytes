# just for testing IEEE floating points
import struct

# 9.75
print(struct.unpack('>f', bytes([0b01000001, 0b00011100, 0x00, 0x00])))

# 3.25
print(struct.unpack('>f', bytes([0b01000000, 0b01010000, 0x00, 0x00])))