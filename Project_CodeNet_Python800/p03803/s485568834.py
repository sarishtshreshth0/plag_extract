import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))
'''
N = ii()
A = li()

ans = 0
for i in range(N):
    a = 0
    b = 0
    max_b = -float('inf')
    max_a = -float('inf')
    for j in range(i, N):
        if (j-i) % 2:
            b += A[j]
            if b > max_b:
                max_b = b
                max_a = a
        else:
            a += A[j]
    dp[max_a][]
    ans = max(ans, max_a)

print(ans)
'''

A, B =li()

if A == B == 1:
    print('Draw')
elif A == 1:
    print('Alice')
elif B == 1:
    print('Bob')
else:
    if A > B:
        print('Alice')
    elif B > A:
        print('Bob')
    else:
        print('Draw')