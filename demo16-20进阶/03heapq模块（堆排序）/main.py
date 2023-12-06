"""
heapq是Python的一个内置模块，它实现了堆队列算法，也就是优先队列算法。
堆是一种特殊的完全二叉树，其中每个节点的值都小于或等于其子节点的值。这个模块提供了多种函数:
https://docs.python.org/zh-cn/3/library/heapq.html
"""
import heapq

list1 = [34,2,24,25,15,54,28,90]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
"""
从 iterable 所定义的数据集中返回前 n 个最大元素组成的列表。 
如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。 
等价于: sorted(iterable, key=key, reverse=True)[:n]。
"""
print(heapq.nlargest(3,list1))
print(heapq.nsmallest(3,list1))
# lambda在Python中是一个非常有用的关键字，它用于创建匿名函数
# 它会返回list2中的两个元素，这两个元素具有最大的'price'值
print(heapq.nlargest(2,list2,key=lambda x:x['price']))
print(heapq.nlargest(2,list2,key=lambda x:x['shares']))

