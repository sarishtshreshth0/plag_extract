import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, a, b = map(int, readline().rstrip().split())
    mod = 10 ** 9 + 7

    ans = pow(2, n, mod) - 1

    nca, ncb = 1, 1

    for i in range(b):
        ncb = ncb * (n - i) % mod
        ncb *= pow(i + 1, mod - 2, mod)
        if i + 1 == a:
            nca = ncb

    print((ans - (nca + ncb)) % mod)


if __name__ == '__main__':
    main()
