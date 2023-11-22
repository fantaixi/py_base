"""
JSON的数据类型和Python的数据类型是很容易找到对应关系
JSON	                 Python
object	                dict
array	                list
string	                str
number (int / real)	    int / float
true / false	        True / False
null	                None

Python	                                        JSON
dict	                                    object
list, tuple	                                array
str	                                        string
int, float, int- & float-derived Enums	    number
True / False	                            true / false
None	                                    null

使用Python中的json模块就可以将字典或列表以JSON格式保存到文件中
"""

"""
json模块主要有四个比较重要的函数，分别是：
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""
import json


def main():
    mydict = {
        'name':'aaa',
        'age':28,
        'qq':9527,
        'friends':['111','222'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print("保存成功")

if __name__ =='__main__':
    main()