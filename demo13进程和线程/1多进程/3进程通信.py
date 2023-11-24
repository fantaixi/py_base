"""
启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个
"""
from multiprocessing import Queue, Process
from time import sleep

"""
from multiprocessing import Process
from time import sleep

counter = 0

def sub_task(string):
    global counter
    while counter <10:
        # flush: 表示输出是否被缓存，默认值是False，如果为True，输出会被强制刷新。
        print(string,end='',flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task,args=("Ping",)).start()
    Process(target=sub_task,args=("Pong",)).start()

if __name__ == '__main__':
    main()
    
"""

"""
输出：
PingPongPingPongPingPongPingPongPingPongPingPongPingPongPingPongPingPongPingPong

在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，
这也就意味着两个子进程中各有一个counter变量，所以结果也就可想而知
"""

"""
改进
"""
def Ping(q):
    for i in range(5):
        q.put('Ping')

def Pong(q):
    for i in range(5):
        q.put('Pong')

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=Ping,args=(q,))
    p2 = Process(target=Pong,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    while not q.empty():
        print(q.get(),end=' ')

