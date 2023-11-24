"""
完成1~100000000求和的计算密集型任务
"""
from time import time


def main():
    total = 0
    number_list =  [x for x in range(1,100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('耗费时间：%.3fs' % (end-start))  # 耗费时间：21.271s

if __name__ == '__main__':
    main()