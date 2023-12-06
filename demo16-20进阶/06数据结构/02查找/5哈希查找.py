# 将数据存储在哈希表中，根据数据的哈希值来查找数据

class HashTable:
    def __init__(self):
        self.table = [None] * 100

    # 在 put() 方法中，首先使用 hash() 函数将键转换为哈希值。然后，将哈希值作为数组的索引。最后，将数据存储在数组中
    def put(self,key,vaule):
        index = hash(key) % len(self.table)
        self.table[index] = vaule

    # 在 get() 方法中，首先使用 hash() 函数将键转换为哈希值。然后，将哈希值作为数组的索引。最后，返回数组中的元素
    def get(self,key):
        index = hash(key) % len(self.table)
        return self.table[index]

hash_table = HashTable()
hash_table.put("1","a")
hash_table.put("2","b")
hash_table.put("3","c")

print(hash_table.get("2"))