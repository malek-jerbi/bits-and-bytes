import struct


def encode(n):
    out = []
    while n > 0 :
        part = n & 0x7f
        n >>= 7
        if n > 0:
            part |= 0x80 # or part |=0b10000000
        out.append(part)
    return bytes(out)

def decode(varn):
    n = 0
    for b in reversed(varn):
        n <<= 7
        n += b & 0x7f
        
    return n


with open('150.uint64', 'rb') as f:
    n = struct.unpack('>Q', f.read())[0]
    assert encode(150) == b'\x96\x01'
    assert decode(b'\x96\x01') == 150