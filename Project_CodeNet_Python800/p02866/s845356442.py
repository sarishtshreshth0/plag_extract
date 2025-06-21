from collections import Counter
import sys
MOD = 998244353


def main():
    n, *d =  map(int, sys.stdin.buffer.read().split())
    D = Counter(d)
    if D[0] != 1:
        print(0)
    else:
        ans = 1
        for i in d[1:]:
            ans = ans*D[i-1]%MOD
        print(ans % MOD)


if __name__ == '__main__':
    main()
