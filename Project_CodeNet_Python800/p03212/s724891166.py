n = int(input())

def func(s):
    if int(s) > n:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += func(s+c)
    return ret

print(func('0'))