import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def com_once(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    numer = denom = 1
    for i in range(r):
        numer = numer * (n - i) % MOD
        denom = denom * (i + 1) % MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


def main():
    n, a, b = map(int, read().split())

    ans = (pow(2, n, MOD) - com_once(n, a, MOD) - com_once(n, b, MOD) - 1) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
