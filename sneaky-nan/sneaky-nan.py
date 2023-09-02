# the function conceal takes in a string and converts it to the floating point NaN
# the function extract takes in a once converted NaN and converts it back to a string


import struct

# 9.75
def conceal(string):
    # convert to bytes
    flt = bytes(string, 'utf-8')
    # the beginning two bytes of a NaN: 0, then eleven 1's, then whatever
    binary_str = '0111111111110000'
    integer_val = int(binary_str, 2)
    # pack them in order into a bytes stream
    bytes_stream = struct.pack('>hb5s',  integer_val, int('00000000'), flt)
    # convert that bytes stream to a float
    concealed = struct.unpack('>d', bytes_stream)[0]
    return concealed

def extract(concealed):
    bytes_stream = struct.pack('>d',  concealed)
    short, i, string = struct.unpack('>hb5s',  bytes_stream)
    string = str(string, encoding='utf-8')
    print(string)

x = conceal('hello')
print(x)
print(type(x))
print(x / 2)

extract(x)