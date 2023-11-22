# 打印如下所示的三角形图案。
'''
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''

'''
在Python中，`print()`函数的`end`参数用于指定输出后应添加的字符串。
默认情况下，`end`的值为`\n`，这意味着在每次调用`print()`函数后，都会添加一个新行。
这就是为什么当我们连续调用`print()`函数时，输出会出现在不同的行上。
然而，我们可以通过更改`end`参数的值来改变这种行为。
例如，如果我们将`end`设置为一个空字符串（`""`），那么`print()`函数将不会在输出后添加任何字符，包括新行。
这就是为什么在上一个例子中，我们使用`end=""`来在同一行上打印多个星号。

以下是一个例子来说明`end`参数的作用：
```python
print("Hello", end="")
print("World")
```

这段代码将输出`HelloWorld`，而不是在两个单词之间添加新行。希望这个解释能帮助你理解`end`参数的作用！
'''
row = int(input("请输入行数:"))

for i in range(row):
    for j in range(i + 1):
        # end="" 参数用于确保在同一行打印多个星号
        print("*", end="")
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()

# 每一行打印的星号数量等于当前行数加一，而空格的数量则等于总行数减去当前行数。
# 例如，第一行打印一个星号和四个空格，第二行打印两个星号和三个空格，以此类推。
for i in range(row):
    print(" " * (row - i - 1) + "*" * (i + 1))

# 每一行打印的星号数量等于当前行数的两倍再加一，而空格的数量则等于总行数减去当前行数。
for i in range(row):
    print(" "*(row-i-1)+"*"*(2*i+1))

for i in range(row):
    for _ in range(row-i-1):
        print(" ",end="")
    for _ in range(2*i+1):
        print("*",end="")
    print()
