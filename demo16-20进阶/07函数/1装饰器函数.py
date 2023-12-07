# 装饰器函数（使用装饰器和取消装饰器）
"""
装饰器函数是Python中的一个重要概念。
简单来说，装饰器是一种特殊的函数，它可以修改其他函数的功能。
装饰器的特殊之处在于它的返回值也是一个函数。
使用装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。

装饰器的使用通常在有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景
"""
from functools import wraps
from time import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()

# 输出函数执行时间的装饰器
def record_time(func):
    """自定义装饰函数的装饰器"""

    # 这是一个装饰器，用于更新被装饰函数的名字和文档字符串。
    # 这样，当你查看被装饰函数的__name__和__doc__属性时，你会看到原始函数的名字和文档字符串，而不是wrapper函数的
    @wraps(func)
    # 定义了一个内部函数wrapper，它接受任意数量的位置参数和关键字参数。
    # 这样，无论func函数需要什么样的参数，wrapper都能正确地传递给它。
    def wrapper(*args,**kwargs):
        start = time()
        result = func(*args,**kwargs)
        # 打印了func函数的名字和它的运行时间
        print(f'{func.__name__}:{time() - start}秒')
        return result
    return wrapper

# 使用
@record_time
def my_func():
    print(99*100)

my_func()

