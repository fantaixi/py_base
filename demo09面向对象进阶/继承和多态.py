"""
可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。
提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力(多态)
"""
from abc import ABCMeta, abstractmethod


class Person(object):
    """人"""
    def __init__(self, name, age):
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
        self._age=age
    def play(self):
        print("%s正在玩耍." % self._name)
    def watch_av(self):
        if self._age >= 18:
            print("%s正在看大片。" % self._name)
        else:
            print("%s你不配。" % self._name)

class Student(Person):
    """学生"""
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def study(self,course):
        print("%s的%s正在学习%s。" % (self._grade,self._name,course))

class Teacher(Person):
    """老师"""
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    def teach(self,course):
        print("%s%s正在讲%s。" % (self._name,self._title,course))

def main():
    stu = Student("啊啊啊",15,"初三")
    stu.study("数学")
    stu.watch_av()
    t = Teacher("aaa",28,"专家")
    t.teach("Python")
    t.watch_av()

if __name__ == '__main__':
    main()

"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态
"""

"""
在Python中，当我们创建类的时候，metaclass可以作为一个参数。
这个参数的主要作用是指定这个类的元类，也就是指定这个类的创建逻辑。
元类（metaclass）是Python中的一个概念，它的作用是定制类的创建行为。
元类是type的子类，通过替换type的__call__运算符重载机制，“超越变形”正常的类
"""

"""
在Python中，metaclass=ABCMeta是一种特殊的元类（metaclass）用法。
ABCMeta是abc模块中定义的一个元类，它用于创建抽象基类（Abstract Base Class，简称ABC）。
当我们在定义一个类时，如果我们指定metaclass=ABCMeta，那么这个类就成为了一个抽象基类。
抽象基类主要用于定义接口，它可以声明一些抽象方法和抽象属性，这些方法和属性必须在任何直接或间接的子类中被实现。
"""
class Pet(object,metaclass=ABCMeta):
    """宠物"""
    def __init__(self,nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发声"""
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

pets = [Dog("旺柴"),Cat("咪咪"),Dog("死狗")]
for pet in pets:
    pet.make_voice()