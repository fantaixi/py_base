# 生成斐波那契数列的前20个数。
# 说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为"兔子数列"。
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
# 形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

a=0
b=1
for _ in range(20):
    a,b = b,a+b
    print(a,end=",")
print()

Fibonacci_sequence = [1,1]
for num in range(2,20):
    sum = Fibonacci_sequence[num-2]+Fibonacci_sequence[num-1]
    Fibonacci_sequence.append(sum)
print(Fibonacci_sequence)
print(len(Fibonacci_sequence))