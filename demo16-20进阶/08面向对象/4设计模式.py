"""
GoF设计模式

创建型模式：单例、工厂、建造者、原型
结构型模式：适配器、门面（外观）、代理
行为型模式：迭代器、观察者、状态、策略

例子：可插拔的哈希算法（策略模式）。
"""
class StreamHasher():
    """哈希摘要生成器"""

    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()

def main():
    """主函数"""
    hasher1 = StreamHasher()
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher2(stream))


if __name__ == '__main__':
    main()