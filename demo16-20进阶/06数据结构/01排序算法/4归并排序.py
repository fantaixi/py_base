"""
归并排序是一种有效的排序算法，它基于归并操作。该算法采用分治法（Divide and Conquer）的一个非常典型的应用。
归并排序的基本思想是将n个元素分成含n/2个元素的子序列，然后对这两个子序列递归地排序，最后将两个已排序的子序列合并以得到排序结果。
归并排序的实现逻辑可以分为迭代法和递归法：
迭代法：
1、申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列。
2、设定两个指针，最初位置分别为两个已经排序序列的起始位置。
3、比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置。
4、重复步骤3直到某一指针到达序列尾。
5、将另一序列剩下的所有元素直接复制到合并序列尾。

递归法：
1、将序列每相邻两个数字进行归并操作，形成floor(n/2)个序列，排序后每个序列包含两个元素。
2、将上述序列再次归并，形成floor(n/4)个序列，每个序列包含四个元素。
3、重复步骤2，直到所有元素排序完毕。
归并排序的平均时间复杂度是O(nlogn)，空间复杂度是O(n)，并且是一种稳定的排序算法
"""


# 递归法
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

arr = [5, 2, 4, 6, 1, 3]
print(mergeSort(arr))

# 迭代法

def mergeSort1(arr):
    n = len(arr)
    # 单个元素默认为有序，从单个元素开始合并
    size = 1
    # 迭代合并子数组
    while size < n:
        # 按照子数组大小，两两合并
        left = 0
        while left < n - size:
            # 计算右子数组的起始索引
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)
            # 合并左右子数组
            merge1(arr, left, mid, right)
            # 更新左子数组的起始索引
            left += 2 * size
        # 每次迭代，子数组大小翻倍
        size *= 2

    return arr

def merge1(arr, left, mid, right):
    # 计算左右子数组的长度
    n1 = mid - left + 1
    n2 = right - mid

    # 创建临时数组
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    # 合并左右子数组
    i = j = 0  # 左右子数组的索引
    k = left  # 合并后的数组索引

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 将左子数组的剩余元素复制到合并后的数组
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 将右子数组的剩余元素复制到合并后的数组
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr1 = [5, 3, 8, 6, 2, 7, 1, 4]
sorted_arr = mergeSort1(arr1)
print(sorted_arr)  # 输出：[1, 2, 3, 4, 5, 6, 7, 8]
