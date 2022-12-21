"""
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
"""

# 在bar函数的内部并没有定义a和b两个变量，那么a和b是从哪里来的。
# 我们在上面代码的if分支中定义了一个变量a，这是一个全局变量（global variable），属于全局作用域，因为它没有定义在任何一个函数中。
# 在上面的foo函数中我们定义了变量b，这是一个定义在函数中的局部变量（local variable），属于局部作用域，在foo函数的外部并不能访问到它；
# 但对于foo函数内部的bar函数来说，变量b属于嵌套作用域，在bar函数中我们是可以访问到它的。
# bar函数中的变量c属于局部作用域，在bar函数之外是无法访问的。
# 事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，前三者我们在上面的代码中已经看到了，
# 所谓的“内置作用域”就是Python内置的那些标识符，我们之前用过的input、print、int等都属于内置作用域。

"""
# 希望通过函数调用修改全局变量a的值，但实际上下面的代码是做不到的
def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100
"""

"""
在调用foo函数后，我们发现a的值仍然是100，这是因为当我们在函数foo中写a = 200的时候，
是重新定义了一个名字为a的局部变量，它跟全局作用域的a并不是同一个变量，因为局部作用域中有了自己的变量a，
因此foo函数不再搜索全局作用域中的a。如果我们希望在foo函数中修改全局作用域中的a，代码如下所示。
"""

"""
def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
"""

"""
使用global关键字来指示foo函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域。
同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域
"""

def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main()
