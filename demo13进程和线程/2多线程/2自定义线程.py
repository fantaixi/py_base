""""
从已有的类创建新类，因此也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程。
"""
from random import randint
from threading import Thread
from time import sleep, time


class DownLoad(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("开始下载%s..." % self._filename)
        time_to_download = randint(5,10)
        sleep(time_to_download)
        print("%s下载完成，耗费了%d秒" % (self._filename,time_to_download))

def main():
    start = time()
    t1 = DownLoad("Python从入门到入狱.pdf")
    t1.start()
    t2 = DownLoad("Tokyo Hot.avi")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("总共耗费了%.3f秒。" % (end-start))

if __name__ == '__main__':
    main()