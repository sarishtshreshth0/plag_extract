from functools import reduce

stdin = open(0)
N, A, B = map(int, stdin.read().split())
MOD = 10 ** 9 + 7


def f(A):
    num = reduce(lambda x, y: x * y % MOD, range(N, N - A, -1))
    den = reduce(lambda x, y: x * y % MOD, range(1, A + 1))
    return num * pow(den, MOD - 2, MOD) % MOD


answer = pow(2, N, MOD) - f(A) - f(B) - 1
answer %= MOD
print(answer)
