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

def g(x):
    if x <= 0:
        return 0
    tmp = x
    n = 0
    while tmp > 0:
        tmp //= 2
        n += 1
    l = [0]*n
    for i in range(n):
        if i==0:
            l[i] = 1 if x%4==1 or x%4==2 else 0
        else:
            l[i] = max(x%(1<<(i+1))-(1<<i)+1, 0)%2
    return sum(l[i]*(2**i) for i in range(n))


def main():
    A, B = mi()
    print(g(B)^g(A-1))

if __name__ == '__main__':
    main()
