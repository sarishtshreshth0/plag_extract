import sys
from math import factorial

MOD = 10 ** 9 + 7


def main():
    # input = sys.stdin.buffer.readline
    n, a, b = map(int, input().split())
    comb_a = 1
    for i in range(a):
        comb_a *= n - i
        comb_a %= MOD
    comb_b = comb_a
    for i in range(a, b):
        comb_b *= n - i
        comb_b %= MOD
    invfact_b = pow(factorial(b), MOD - 2, MOD)
    invfact_a = invfact_b
    for i in range(b, a, -1):
        invfact_a *= i
        invfact_a %= MOD
    comb_a *= invfact_a
    comb_a %= MOD
    comb_b *= invfact_b
    comb_b %= MOD
    print((pow(2, n, MOD) - 1 - comb_a - comb_b) % MOD)


if __name__ == "__main__":
    main()
