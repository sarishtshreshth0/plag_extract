import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)
MOD = 998244353


def main():
    N = int(input())
    D = list(map(int, input().split()))
    C = Counter(D)
    if D[0] != 0:
        print(0)
    elif C[0] > 1:
        print(0)
    else:
        ans = 1
        key = list(C.keys())
        key.sort()
        l = len(key)
        for i in range(1, l):
            if key[i - 1] + 1 != key[i]:
                a = 0
            else:
                a = C[key[i - 1]] ** C[key[i]]
            ans *= a
            ans %= MOD
            if ans == 0:
                break
        print(ans)


if __name__ == "__main__":
    main()
