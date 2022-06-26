def int32_to_ip(int32):
    v1 = int32 & 0xff
    v2 = (int32 >> 8) & 0xff
    v3 = (int32 >> 16) & 0xff
    v4 = (int32 >> 24)
    return f"{v4}.{v3}.{v2}.{v1}"


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

