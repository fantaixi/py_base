"""
如果open函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。
为了让代码有一定的健壮性和容错性，我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理
"""

"""
在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，
在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况。
例如在上面读取文件的过程中，文件找不到会引发FileNotFoundError，指定了未知的编码会引发LookupError，
而如果读取文件时无法按指定方式解码会引发UnicodeDecodeError，我们在try后面跟上了三个except分别处理这三种不同的异常状况。
最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，
由于finally块的代码不论程序正常还是异常都会执行到
（甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），
因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。
"""

def main():
    f = None
    try:
        f = open("aaa.txt","r",encoding="utf-8")
        print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件")
    except LookupError:
        print("未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
