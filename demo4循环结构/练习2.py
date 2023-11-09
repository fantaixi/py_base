# 输入两个正整数，计算它们的最大公约数和最小公倍数。
# 提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

a = int(input("a = "))
b = int(input("b = "))
if a > b:
    a, b = b, a
for num in range(a, 0, -1):
    if a % num == 0 and b % num == 0:
        print("最小公倍数是%d" % num)
        print("最大公约数是%d" % (a * b / num))
        break
