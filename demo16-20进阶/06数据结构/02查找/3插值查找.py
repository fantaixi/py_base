# 根据目标元素的值，估算其在数组中的位置，然后从该位置开始进行查找

def insert_search(item, key):
    left = 0
    right = len(item) - 1
    while left <= right:
        mid = left + (key - item[left]) / (item[right] - item[left]) * (right - left)
        if item[mid] == key:
            return mid
        elif item[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1
