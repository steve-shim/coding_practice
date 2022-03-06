import hashlib

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key): # 해시 값을 구한다
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

hash = ChainedHash(10)
print(hash.hash_value(17))
print(hash.hash_value('test'))

# for i in [1,2,3.163,4,5]:
#     print(f'{i:*>5.1f}', end=' ') # **1.0 **2.0 **3.2 **4.0 **5.0
