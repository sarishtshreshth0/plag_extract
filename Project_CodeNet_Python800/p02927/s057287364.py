import sys, math
from functools import lru_cache
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
    M, D = mi()
    cnt = 0

    for m in range(1, M+1):
        for d in range(1, D+1):
            if d > 9:
                d1 = int(str(d)[1])
                d10 = int(str(d)[0])

                if d1 >= 2 and d10 >= 2 and d1*d10 == m:
                    cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()