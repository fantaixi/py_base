list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)

# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
print("------------------------------")

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
print("------------------------------")

# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
print("------------------------------")

# 清空列表元素
list1.clear()
print(list1) # []
print("------------------------------")

# 和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
print("------------------------------")

# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
print("------------------------------")

# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
print("---------------------------------")

# 对列表的排序操作
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
# reverse （可选） - 如果True，则排序列表被反转（或按降序排序）。False如果未提供则默认为。
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# key（可选） - 用作排序比较键的函数。默认为None.
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
print("------------------------------")

# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
print(list4)
list1.sort(reverse=False)
print(list1)

"""
sorted()函数返回的是一个新的列表，原始的列表不会被改变。
这与列表对象的.sort()方法不同，后者会直接修改原始的列表。
此外，sorted()函数可以对任何可迭代的对象进行排序，而.sort()方法只能用于列表。
"""