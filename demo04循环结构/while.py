"""
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True则继续循环；表达式的值为False则结束循环。
"""
import random

"""
计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""
answer = random.randint(1,100)
count = 0
while True:
    count += 1
    num = int(input("请输入:"))
    if num < answer:
        print("猜得小了")
    elif num > answer:
        print("猜得大了")
    else:
        print("对了")
        # 使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，
        # 这一点在使用嵌套的循环结构（下面会讲到）需要引起注意
        break
print("总共猜了%d次" % count)
if count > 7:
    print("你完了")

