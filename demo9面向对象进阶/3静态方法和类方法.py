"""
之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
实际上，我们写在类中的方法并不需要都是对象方法，
"""
from math import sqrt
from time import localtime, time, sleep

"""
@staticmethod是一个装饰器，用于修饰类中的方法。它的主要作用和用法如下：

无需实例化：通常，如果我们想使用某个类的方法，我们需要先创建一个类的实例，然后通过这个实例来调用方法。
但是，如果我们使用了@staticmethod来修饰一个方法，那么我们就可以直接通过类名来调用这个方法，而无需创建类的实例。

执行效率高：由于无需创建类的实例，因此使用@staticmethod修饰的方法的执行效率会比较高。

无法引用类属性或方法：@staticmethod修饰的方法不能引用类中的其他属性或方法，也就是说，它们在方法体内部不能使用self。

代码组织和可读性：@staticmethod可以帮助我们更好地组织代码，将一些与类相关的功能性方法放在类中，这样可以提高代码的结构和程序的可读性
"""

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()

print("----------------------------")

"""
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
"""

"""
@classmethod是一个装饰器，用于将类中的方法声明为类方法。它的主要作用和用法如下：
类方法：@classmethod装饰的方法是类方法，可以直接通过类名来调用，也可以通过类的实例来调用。
访问类属性：类方法的第一个参数通常是cls，它表示类本身，可以用来访问类的属性。
不能访问实例属性：类方法只能访问类属性，不能访问实例属性。
工厂方法：类方法可以作为工厂方法，用于创建类的实例。
"""
class Clock(object):
    def __init__(self,hour =0,minute=0,second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute =0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)

clock = Clock.now()
while True:
    print(clock.show())
    sleep(1)
    clock.run()

"""
类之间的关系
简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。

has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；
关联关系如果是整体和部分的关联，那么我们称之为聚合关系；
如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。

use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
"""

