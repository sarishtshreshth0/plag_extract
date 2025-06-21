a, b = map(int, input().split())
def f(x):
    if (x + 1) % 4 == 0:
        return 0
    elif (x + 1) % 4 == 1:
        return x
    elif (x + 1) % 4 == 2:
        return x ^ (x - 1)
    else:
        return x ^ (x - 1) ^ (x - 2)
print(f(b) ^ f(a - 1))