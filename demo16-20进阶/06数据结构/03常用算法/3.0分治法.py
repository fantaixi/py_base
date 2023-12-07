# 把一个复杂的问题分成两个或更多的相同或相似的子问题，
# 再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解

# 给定一个无序的数组，将其排序

def merge_sort(arr):
    # 基本情况：如果数组只有一个元素，那么它已经排序了
    if len(arr) <= 1:
        return arr

    # 将数组分为两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 递归地排序两半
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 合并排序后的两半
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index<len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

     # 如果任何一半还有剩余的元素，将它们添加到结果中
    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1
    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1

    return merged

# 测试
arr = [38, 27, 43, 3, 9, 82, 10,0]
print(merge_sort(arr))