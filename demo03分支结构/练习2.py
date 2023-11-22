# 输入三条边长，如果能构成三角形就计算周长和面积

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
   mid = (a+b+c)/2
   area = (mid * (mid - a)*(mid-b)*(mid-c)) ** 0.5
   print("面积=%.2f,周长=%.f" % (area,a+b+c))
else:
    print("不能构成三角形")
