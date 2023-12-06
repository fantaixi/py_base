"""
冒泡排序（Bubble Sort）是一种简单直观的排序算法。它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
以下是冒泡排序的基本步骤：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
"""

arr = [1,10,99,77,88]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort(arr))

# 优化
# 1、设置标志位：如果在某一趟排序中没有发生元素交换，说明这组数据已经有序，不用再继续下去
def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # 设置标志位
                flag = 1
        if flag == 0:
            break
    return arr

print(bubble_sort1(arr))

# 2、设置结束边界：记录最后一次交换的位置，后面没有交换，必然是有序的，然后下一次排序从第一个比较到上次记录的位置结束即可
def bubble_sort2(arr):
    n = len(arr)
    k = n-1
    for i in range(n):
        flag = 0
        for j in range(0,k):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
                # 设置结束边界
                k = j
        if flag == 0:
            break
    return arr

print(bubble_sort2(arr))

# 3、双向冒泡排序：这个优化是在每次遍历中，先正向遍历找到最大值放到最后，然后反向遍历找到最小值放到最前面。
# 这样每次遍历可以确定两个元素的位置，可以减少遍历的次数
def bubble_sort3(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(i,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        for j in range(n-i-1,i,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                flag = 1
        if flag == 0:
            break
    return arr

arr1 = [1,10,99,77,88,66,11]
print(bubble_sort3(arr1))


