#Binary Data Type:
# Bytes, ByteArray (range: 0-256)

numbers = [0,1,2,4,6,123,255]
n = bytes(numbers)
print(type(n))

numbers1 = [0,1,2,4,6,123,255]
n1 = bytearray(numbers1)
n1[3]= 145
print(n1[3])