# 输入一个正整数判断是不是素数。
# 提示：素数指的是只能被1和自身整除的大于1的整数。
import math

num = int(input("请输入一个正整数："))
end = int(math.sqrt(num))
#用来控制退出循环的条件
is_Prise = True
for x in range(2, end + 1):
    if num % x == 0:
        is_Prise = False
        break
if is_Prise and num != 1:
    print("%d 是素数" % num)
else:
    print("%d 不是素数" % num)
