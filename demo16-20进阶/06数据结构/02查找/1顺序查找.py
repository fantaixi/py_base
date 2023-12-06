def seq_search(item,key):
    # 首先，使用 enumerate() 函数将数组的每个元素及其索引组成一个元组，并将其赋给 item 变量。
    # 然后，使用 for 循环遍历 item 变量，每次循环都将当前元素的值赋给 item 变量。
    for index,item in enumerate(item):
        if item == key:
            return index
    return -1

# def seq_search(item, key):
#     for i in range(len(item)):
#         if item[i] == key:
#             return i
#     return -1

item = [1, 2, 3, 4, 5]
key = 3
print(seq_search(item,key))
