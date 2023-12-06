# 生成式（推导式）的用法
# 生成式（推导式）是一种在 Python 中创建数据结构的简洁方法，可以用来生成列表、集合和字典。
# 它可以将循环和条件判断相结合，从而避免语法冗长的代码

"""
格式如下:

生成式（推导式）的基本格式如下：
1. 列表推导式：[expression for item in iterable if condition]
2. 字典推导式：{key_expression: value_expression for item in iterable if condition}
3. 集合推导式：{expression for item in iterable if condition}
4. 生成器推导式：(expression for item in iterable if condition)
其中：
- expression 是根据 `item` 计算得出的表达式。
- item 是 `iterable` 中的元素。
- iterable 是任何可迭代的对象。
- condition 是可选的过滤条件。
"""

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 用股票价格大于100块的股票构造一个新字典
prices2 = {key: value for key,value in prices.items() if value>100}
print(prices2)

# 1、列表推导式：这是最常见的推导式，可以快速生成列表。例如，生成1到10之间的数字的平方的列表
nums = [i*i for i in range(1,11)]
print("nums1=",nums)

# 2、带条件的推导式：可以在推导式中加入条件判断，例如生成一个列表，包含1到10之间是3的倍数的数字
nums2 = [i*i for i in range(1,11) if i %3 ==0]
print("nums2=",nums2)

# 3、带条件的表达式：可以在推导式中使用if-else语句，例如生成一个列表，如果是3的倍数就用平方，否则就用数字本身
nums3 = [i*i if i % 3 ==0 else i for i in range(1,11)]
print("nums3=",nums3)

# 4、生成器推导式：生成器推导式的用法与列表推导式非常相似，但在形式上生成器推导式使用圆括号（parentheses）作为定界符，
# 而不是列表推导式所使用的方括号（square brackets）。生成器只有在调用的时候才会把数据拿出来，占用内存
# 生成器对象本身并不能直接查看，它们是用于生成数据的工具。
# 如果你想查看生成器生成的所有值，你可以使用 list() 函数将其转换为列表
nums4 = (i*i for i in range(1,11))
print("nums4=",list(nums4))

# 5、字典推导式：推导字典的方式和推导列表很相似，只不过使用大括号，并且使用键值对
nums_dict = {n:n*n for n in range(1,11)}
print("nums_dict=",nums_dict)

# 6、集合推导式：推导集合的方式和列表是一样的，区别在于使用大括号，类似于推导字典，但它是单个元素，而不是键值对。
# 集合会自动过滤掉重复的元素

# 基本的集合推导式：例如，生成1到10之间所有偶数的集合
evens = {x for x in range(1,11) if x % 2 ==0}
print("evens=",evens)

# 带条件的集合推导式：例如，生成一个集合，包含1到10之间所有偶数的平方
sq = {x**2 for x in range(1,11) if x %2 ==0}
print("sq=",sq)  # 生成的集合乱序

# 集合推导式的去重功能：集合推导式会自动去除重复的元素。例如，如果我们有一个包含重复元素的列表，我们可以使用集合推导式来去除重复元素
nums_n = [1,1,2,2,2,3,3,4,4,4,4,5]
unique_num = {x for x in nums_n}
print("unique_num=",unique_num)