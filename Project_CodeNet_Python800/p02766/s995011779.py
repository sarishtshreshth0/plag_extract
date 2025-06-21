from string import printable
def func1(x, b):
    assert(x >= 0)
    assert(1< b < 37)
    r = ''
    while x > 0:
        r = printable[x % b] + r
        x //= b
    return r
def func2(s, b):
    assert(1 < b < 37)
    return int(s, b)
def convert(s, a, b):
    return func1(func2(s, a), b)
n, k= map(int, input().split())
x=convert(str(n), 10, k)
print(len(x))