"""
如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，
通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示。
"""
def main():
    try:
        with open("aaa.txt","r",encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件")
    except LookupError:
        print("未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")

if __name__ == '__main__':
    main()