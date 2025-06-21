N = int(input())
def func(value):
    return value if value%2 == 0 else 2*value
print(func(N))