a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))  #  ** 表示阶乘
# %d是整数的占位符，%f是小数的占位符，
# %%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），