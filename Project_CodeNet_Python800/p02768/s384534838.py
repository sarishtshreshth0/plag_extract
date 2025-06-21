N, A, B = [int(_) for _ in input().split()]
MOD = 10 ** 9 + 7
var1 = pow(2, N, MOD) - 1


def f(x):
    f1 = 1
    for i in range(N - x + 1, N + 1):
        f1 = (f1 * i) % MOD

    # 逆元
    f2 = 1
    for i in range(2, x + 1):
        f2 = (f2*i)%MOD
    f2 = pow(f2, MOD - 2, MOD)
    return (f1 * f2) % MOD


ans = var1 - f(A) - f(B)
print(ans % MOD)
