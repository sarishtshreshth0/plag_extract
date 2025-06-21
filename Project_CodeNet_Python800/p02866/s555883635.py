from collections import Counter
import sys
MOD = 998244353


def main():
    n, *d = map(int, sys.stdin.buffer.read().split())
    e = [0]*n
    for i in d:
        e[i] += 1
    ans = e[0]
    for i in d[1:]:
        ans *= e[i-1]
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
