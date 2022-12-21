# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
# 例如：$1^3 + 5^3+ 3^3=153$。
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 +mid **3 +high**3:
        print(num)

# 将一个正整数反转，例如：将12345变成54321
num  = int(input("num = "))
reversed_num = 0
while num >0:
    reversed_num = reversed_num *10 + num % 10
    num //= 10
print(reversed_num)