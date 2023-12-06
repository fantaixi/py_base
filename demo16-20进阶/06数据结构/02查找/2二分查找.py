def bin_search(item, key):
    left = 0
    right = len(item) - 1
    while left <= right:
        mid = (left + right) // 2
        if item[mid] == key:
            return mid
        elif item[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

item = [1, 2, 3, 4, 5]
key = 3
print(bin_search(item,key))