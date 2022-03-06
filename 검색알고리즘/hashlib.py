import hashlib
'''
SHA1: 20바이트(160bits)
SHA256: 32바이트(256bits)
SHA384: 48바이트(384bits)
SHA512: 64바이트(512bits)
'''
data = 'test'.encode()
print(data)
hash_object = hashlib.sha1()
hash_object.update(b'test')
# hash_object.update(data)
hex_dig = hash_object.hexdigest()
print( "[1]", hex_dig, len(hex_dig), type(hex_dig) ) # len: 40 -> 20Byte
print( "[2]", hashlib.sha1('test'.encode()).hexdigest() )
# 'test' 값의 sha1 이라는 hash함수를 통해 나온 hash 값의 16 진수 변환상태
# a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
print( int( hashlib.sha1('test'.encode()).hexdigest(), 16 ) )
# 16 진수 -> 10 진수
print( hex( int( hashlib.sha1('test'.encode()).hexdigest(), 16 ) ))
# 10 진수 -> 16 진수
print( "[sha256]", hashlib.sha256('test'.encode()).hexdigest() , len(hashlib.sha256('test'.encode()).hexdigest()))
# len: 64 -> 32Bytes

print(int('0xFF', 16))      # 16진수 -> 10진수 
print(int('0b11111111', 2)) # 8bit -> 1Byte