# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random
import string


def rand_code(code_len=6):
    all_chars = "1234567890qwertyuiopadfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

# 随机生成一个六位数的验证码
def rand_code1(code_len=6):
    all_num = "0123456789"
    last_pos = len(all_num)-1
    code = ""
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_num[index]
    return code

print(rand_code(6))
print(rand_code1(6))


def generate_verification_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

# 调用函数生成长度为6的验证码
code = generate_verification_code(6)
print(code)