"""
除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
"""
import time


def main():
    # 一次性读取整个文件
    with open("aaa.txt","r",encoding="utf-8") as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open("aaa.txt","r",encoding="utf-8") as f:
        for line in f:
            print(line,end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open("aaa.txt") as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()