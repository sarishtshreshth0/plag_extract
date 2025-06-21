a, b = map(int, input().split())
def f(x):
    return 0 if x <= 0 else x >> 1 & 1 ^ 1 if x & 1 else f(x - 1) | x
print(f(b) ^ f(max(0, a - 1)))