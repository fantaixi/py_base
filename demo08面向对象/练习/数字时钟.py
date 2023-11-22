# 定义一个类描述数字时钟。
"""
from time import sleep

class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def run(self):
        self.__second += 1
        if self.__second == 60:
            self.__second =0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def show(self):
        return "%02d:%02d:%02d" % (self.__hour,self.__minute,self.__second)

def main():
    clock = Clock(23,59,58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == "__main__":
    main()
"""



import threading
import time
from datetime import datetime


class Clock(object):
    def __init__(self):
        self._running = True
        self._thread = threading.Thread(target=self._run)

    def _run(self):
        while self._running:
            now = datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M:%S"),end="\n")
            time.sleep(1)

    def start(self):
        self._thread.start()
    def stop(self):
        self._running = False
        self._thread.join()
def main():
    clock = Clock()
    clock.start()
    time.sleep(10)  # 运行10秒钟
    clock.stop()

if __name__ == "__main__":
    main()