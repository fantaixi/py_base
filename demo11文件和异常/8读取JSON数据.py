import json


def main():
    try:
        with open('data.json','r',encoding='utf-8') as f:
            obj = json.load(f)
            print(obj)
    except FileNotFoundError as e:
        print(e)
        print("找不到文件")
    except json.JSONDecodeError as e:
        print(e)
        print("JSON格式不正确")
    except Exception as e:
        print(e)
        print("未知错误")

if __name__ == '__main__':
    main()