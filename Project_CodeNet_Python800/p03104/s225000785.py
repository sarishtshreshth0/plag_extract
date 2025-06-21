def calc(n):
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return 1 ^ n
    elif n % 4 == 3:
        return 0
    else:
        return 0 ^ n


A, B = map(int, input().split())
print(calc(B) ^ calc(A - 1))
