"""
Unix和Linux操作系统上提供了fork()系统调用来创建进程，
调用fork()函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。
fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，而子进程中的返回值永远都是0。
Python的os模块提供了fork()函数。
由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，
而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。
"""
from random import randint
from time import sleep, time

"""
用一个下载文件的例子来说明使用多进程和不使用多进程到底有什么差别
"""
def download_task(filename):
    print("开始下载%s..." % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print("%s下载完成，耗费了%d秒" % (filename,time_to_download))

def main():
    start = time()
    download_task("Python从入门到入狱.pdf")
    download_task("Tokyo Hot.avi")
    end = time()
    print("总共耗费了%.3f秒。" % (end-start))

if __name__ == '__main__':
    main()

"""
输出如下：

开始下载Python从入门到入狱.pdf...
Python从入门到入狱.pdf下载完成，耗费了8秒
开始下载Tokyo Hot.avi...
Tokyo Hot.avi下载完成，耗费了8秒
总共耗费了16.016秒。
"""