# 逻辑运算符有三个，分别是and、or和not。
# and字面意思是“而且”，所以and运算符会连接两个布尔值，如果两个布尔值都是True，那么运算的结果就是True；左右两边的布尔值有一个是False，最终的运算结果就是False。
# 相信大家已经想到了，如果and左边的布尔值是False，不管右边的布尔值是什么，最终的结果都是False，所以在做运算的时候右边的值会被跳过（短路处理），
# 这也就意味着在and运算符左边为False的情况下，右边的表达式根本不会执行。
#
# or字面意思是“或者”，所以or运算符也会连接两个布尔值，如果两个布尔值有任意一个是True，那么最终的结果就是True。
# 当然，or运算符也是有短路功能的，在它左边的布尔值为True的情况下，右边的表达式根本不会执行。
#
# not运算符的后面会跟上一个布尔值，它的作用是得到与该布尔值相反的值，也就是说，后面的布尔值如果是True运算结果就是False，而后面的布尔值如果是False则运算结果就是True。

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False