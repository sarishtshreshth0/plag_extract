import sys
from math import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, x, *X = map(int, read().split())

    ans = abs(X[0] - x)
    for i in range(1, N):
        ans = gcd(ans, X[i] - x)

    print(ans)
    return


if __name__ == '__main__':
    main()
