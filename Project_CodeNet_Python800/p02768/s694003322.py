import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, a, b = map(int, readline().split())

    ans = pow(2, N, MOD) - 1
    ans %= MOD

    def comb_mod(n, r):
        res = 1
        r = min(n - r, r)

        for i in range(r):
            res *= (n - i)
            res %= MOD
            res *= pow((r - i), MOD - 2, MOD)

        return res

    ans -= comb_mod(N, a)
    ans -= comb_mod(N, b)
    ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
