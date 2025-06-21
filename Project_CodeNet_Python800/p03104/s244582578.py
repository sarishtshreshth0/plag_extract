a,b = map(int, input().split())

def f(x):
    if x % 2 == 1:
        return x // 2 % 2
    return x ^ f(x - 1)

print(f(a-1) ^ f(b))