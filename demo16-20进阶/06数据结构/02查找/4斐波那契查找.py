# 使用斐波那契数列来确定查找的步骤
# 类似于二分查找和插值查找，但是将数组的长度划分为斐波那契数列中的两个相邻数之和，
# 根据待查找元素与数组中间元素的比较结果确定待查找元素所在位置
def fib_search(item, key):
    a, b = 0, 1
    while b < len(item):
        a, b = b, a + b
    i = 0
    while a > 0:
        if item[i] == key:
            return i
        elif item[i] < key:
            a, i = a // 2, i + a
        else:
            b, i = b // 2, i
    return -1
