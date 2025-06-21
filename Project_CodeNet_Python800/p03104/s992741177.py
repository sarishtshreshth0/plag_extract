import sys

def S(): return sys.stdin.readline().rstrip()

A,B = map(int,S().split())

def f(n):  # 0からnまでのxor
    res = 0
    for i in range(41):  # 2**iの位
        if i == 0:
            res += ((n+1)//2) % 2
        else:
            a = n - ((n >> (i+1)) << (i+1))
            if a < 2**i or a % 2 == 1:
                continue
            else:
                res += 1 << i
    return res

print(f(B) ^ f(A-1))