"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
list1 = itertools.permutations('ABCD')
print(list(list1))

# 产生ABCDE的五选三组合
list2 = itertools.combinations('ABCDE',3)
print(list(list2))

# 产生ABCD和123的笛卡尔积
list3 = itertools.product('ABCD','123')
print(list(list3))

# 产生ABC的无限循环序列
list4 = itertools.cycle(('A','B','C'))
# print(list(list4))