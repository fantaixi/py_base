# 在对问题求解时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解
"""
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

名称	    价格（美元）	重量（kg）
电脑	    200	            20
收音机	20	            4
钟	    175	            10
花瓶	    50	            2
书	    10	            1
油画	    90	            9
"""

"""
class Thing(object):
    # 物品
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        # 价格重量比
        return self.price/self.weight

def input_thing():
    # 输入物品信息
    name_str,price_str,weight_str = input().split()
    return name_str,int(price_str),int(weight_str)

def main():
    max_weight,num_of_things = map(int,input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x:x.value,reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f"小偷拿走了{thing.name}")
            total_weight += thing.weight
            total_price += thing.price
    print(f"总价值：{total_price}美刀")

if __name__ == '__main__':
    main()
"""


def knapsack_greedy(items, max_weight):
    # 按照价值重量比排序物品
    items.sort(key=lambda x: x[1]/x[2], reverse=True)

    total_value = 0
    chosen_items = []

    for item in items:
        item_name, item_value, item_weight = item
        # 如果当前物品可以完全装入背包，就将其添加到背包
        if max_weight >= item_weight:
            chosen_items.append(item_name)
            total_value += item_value
            max_weight -= item_weight
        # 如果当前物品不能完全装入背包，就只装入部分
        else:
            fraction = max_weight / item_weight
            chosen_items.append(f"{item_name} ({fraction*100:.1f}%)")
            total_value += item_value * fraction
            break

    return total_value, chosen_items

# 测试
items = [("电脑", 200, 20), ("收音机", 20, 4), ("钟", 175, 10), ("花瓶", 50, 2), ("书", 10, 1), ("油画", 90, 9)]
max_weight = 20
print(knapsack_greedy(items, max_weight))
