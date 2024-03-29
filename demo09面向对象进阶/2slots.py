"""
需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用
"""
class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age >= 16:
            print('%s 正在打飞机.' % self._name)
        else:
            print('%s 正在学习.' % self._name)

def main():
    p = Person('啊对对对', 22)
    p.play()
    p._gender = "男"
    print(p._age)

if __name__ == '__main__':
    main()