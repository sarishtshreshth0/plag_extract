import sys
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
    a = list(mi())
    l = [0]*(10**5)
    m = -1
    for i in range(N):
        l[a[i]] += 1
    for i in range(10**5-2):
        t = l[i]+l[i+1]+l[i+2]
        m = max(m, t)
    print(m)


if __name__ == '__main__':
    main()
