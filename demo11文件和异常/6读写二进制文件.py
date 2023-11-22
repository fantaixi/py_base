"""
复制图片文件
"""
def main():
    try:
        with open("111.png","rb") as fs1:
            data = fs1.read()
            print(type(data))
        with open("bbb.png","wb") as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print(e)
        print("指定的文件无法打开")
    except IOError as e:
        print(e)
        print("读写文件错误")
    print("success")

if __name__ =='__main__':
    main()