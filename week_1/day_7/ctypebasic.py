import ctypes

a = "Hello World"
address = id(a)
# This reaches into memory at that address and pulls the string out
print(ctypes.string_at(a)) # b'H'
print(ctypes.string_at(address)) # b'\x03'
