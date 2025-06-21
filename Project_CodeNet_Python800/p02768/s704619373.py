n, a, b = list(map(int, input().split()))

P = 10 ** 9 + 7


def conb(n, r):
    P = 10 ** 9 + 7
    x = 1
    y = 1
    for i in range(n - r + 1, n + 1):
        x = (x * i % P)
    for i in range(1, r + 1):
        y = (y * i % P)
    y_inv = pow(y, P - 2)
    return x * y_inv


def pow(x, n):
    ans = 1
    while (n > 0):
        if (bin(n & 1) == bin(1)):
            ans = (ans * x) % P
        x = (x * x) % P
        n = n >> 1  # ビットシフト
    return ans


print((pow(2, n) - conb(n, a) - conb(n, b) - 1) % P)
