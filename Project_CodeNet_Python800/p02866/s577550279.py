import sys, math
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    D = list(mi())
    ans = 1

    if D[0] != 0:
        print(0)
        return

    dic = defaultdict(int)
    for i in range(N):
        dic[D[i]] += 1

    for i in range(1, N):
        ans *= dic[D[i]-1]
        ans %= 998244353

    print(ans)

if __name__ == '__main__':
    main()