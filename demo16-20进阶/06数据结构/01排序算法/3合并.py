"""合并(将两个有序的列表合并成一个有序的列表)"""
def merge(items1,items2,comp = lambda x,y:x < y):
    items = []
    index1,index2 = 0,0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

items1 = [1,2,5]
items2 = [3,4,999]
print(merge(items1,items2))
