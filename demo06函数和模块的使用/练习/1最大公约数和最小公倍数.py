def gcd(x, y):
    '''最大公约数'''
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    '''最小公倍数'''
    return x * y // gcd(x, y)

print(gcd(15,25))
print(lcm(15,25))
