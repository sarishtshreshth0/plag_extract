
A, B = map(int, input().split())


def func(n):
    res = 0 if ((n + 1) // 2) % 2 == 0 else 1
    res ^= n if n % 2 == 0 else 0
    return res


print(func(B) ^ func(A - 1))
