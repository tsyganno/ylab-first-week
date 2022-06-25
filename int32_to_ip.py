def int_to_ipv4(int32):
    v1 = int32 & 0xff
    v2 = (int32 >> 8) & 0xff
    v3 = (int32 >> 16) & 0xff
    v4 = (int32 >> 24)
    return f"{v4}.{v3}.{v2}.{v1}"


print(int_to_ipv4(2149583361))
print(int_to_ipv4(32))
print(int_to_ipv4(0))
print(int_to_ipv4(2154959208))
print(int_to_ipv4(2149583361))

