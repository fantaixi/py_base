# 在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。
# 在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，
# 程序中函数的参数就相当于是数学上说的函数的自变量，而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量。

"""
输入M和N计算C(M,N)
阶乘
"""

def fac(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input("m = "))
n = int(input("n = "))
print(fac(m) // fac(n) // fac(m-n))


