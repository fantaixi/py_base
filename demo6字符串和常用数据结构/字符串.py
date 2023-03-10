# 字符串，就是由零个或多个字符组成的有限序列，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串。
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

"""
可以在字符串中使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义，
例如：\n不是代表反斜杠和字符n，而是表示换行；
而\t也不是代表反斜杠和字符t，而是表示制表符。
所以如果想在字符串中表示'要写成\'，同理想表示\要写成\\。
"""

s3 = '\'hello,world\''
s4 = '\n\\hello\\\n'
print(s3,s4,end="")

# 在\后面还可以跟一个八进制或者十六进制数来表示字符，
# 例如\141和\x61都代表小写字母a，前者是八进制的表示法，后者是十六进制的表示法。
# 也可以在\后面跟Unicode字符编码来表示字符

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2,end=" ")
print()

# 如果不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

# 可以使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，
# 可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
# 我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算）

# 切片操作符在python中的原型是
# [start:stop:step]
# 即：[开始索引:结束索引:步长值]
# 开始索引：同其它语言一样，从0开始。序列从左向右方向中，第一个值的索引为0,最后一个为-1
# 结束索引：切片操作符将取到该索引为止，不包含该索引的值。
# 步长值：默认是一个接着一个切取，如果为2,则表示进行隔一取一操作。步长值为正时表示从左向右取，如果为负，则表示从右向左取。步长值不能为0

s1 = 'hello' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print("ll" in s1)
print("aab" in s1)
str2 = "abc123456"
# 从字符串中取出指定位置的字符（下标运算）
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[2::])  # c123456
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45



