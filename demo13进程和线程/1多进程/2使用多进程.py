"""
如果程序中的代码只能按顺序一点点的往下执行，那么即使执行两个毫不相关的下载任务，
也需要先等待一个文件下载完成后才能开始下一个下载任务，
很显然这并不合理也没有效率。
接下来我们使用多进程的方式将两个下载任务放到不同的进程中，代码如下所示。
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep, time


def download_task(filename):
    print("启动下载进程，进程号[%d]." % getpid())
    print("开始下载%s..." % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print("%s 下载完成，耗费了%d秒" % (filename,time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task,args=("Python从入门到入狱.pdf",))
    p1.start()
    p2 = Process(target=download_task,args=("Tokyo Hot.avi",))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("总共耗费了%.3f秒。" % (end-start))

if __name__ == '__main__':
    main()

"""
启动下载进程，进程号[952].
开始下载Python从入门到入狱.pdf...
启动下载进程，进程号[13940].
开始下载Tokyo Hot.avi...
Python从入门到入狱.pdf 下载完成，耗费了6秒
Tokyo Hot.avi 下载完成，耗费了8秒
总共耗费了8.154秒。
"""

"""
通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，
后面的args是一个元组，它代表了传递给函数的参数。
Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时间将大大缩短，不再是两个任务的时间总和。
"""

"""
Process类的基本语法如下：

Process([group [, target [, name [, args [, kwargs]]]]])
其中，group参数未使用，值始终为None。
target表示调用的对象，就是子进程要执行的任务。
name可以为子进程命名。
args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号。
kwargs指定的为传给target函数的关键字参数，是一个字典形式。

Process类的主要方法有：
start(): 启动进程，并调用该子进程中的run()方法。
run(): 进程启动时运行的方法，就是它去调用target指定的函数，我们自定义类的类中一定要实现该方法。
terminate(): 强制终止进程。不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用此方法需要小心：
如果此进程还保存了一个锁那么也将不会释放这个锁，进而导致死锁。
is_alive(): 判断进程是否是“活着”的状态。
join(timeout): 让主进程等待某一子进程结束，才继续执行主进程。timeout是可选的超时时间。超过一个时间主进程就不等待了。

Process类的主要属性有：
daemon: 默认值为False，如果设为True，代表p为后台运行的守护进程，
当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置。
name: 进程的名称。
pid: 进程的pid。
exitcode: 进程在运行时为None、如果为–N，表示被信号N结束。
authkey: 进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。
这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功。

创建Process对象的两种方式：

方式一：直接实例化Process类，传入target参数和args参数，分别指定要执行的函数和函数的参数。
方式二：继承Process类，重写run()方法，将要执行的任务写在run()方法中。
在Windows系统中，创建Process对象必须放在if __name__ == '__main__':下，否则会出现无限递归的情况。
"""