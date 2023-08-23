

with open('teapot.bmp', 'rb') as f:
    hex_content = f.read()
  
offset = hex_content[10]

print("first two pixels: ", hex_content[offset:offset+6])
height = hex_content[22:26]
width = hex_content[18:22]

print("height", height)
print("width", width)

# 00 00 01 a4 = 420

# convert little endian hex to decimal
def little_endian_to_decimal (little_endian):
    decimal = 0
    for i in range(len(little_endian)):
      decimal += (little_endian[i] << 8*i)
    return decimal

height_decimal = little_endian_to_decimal(height)
width_decimal = little_endian_to_decimal(width)

print(width_decimal)