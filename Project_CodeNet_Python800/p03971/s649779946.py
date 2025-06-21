import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()
S = list(input())
a, b = 0, 0
for s in S:
    if s=='c':
        print('No')
        continue
    if s=='a':
        if a+b<A+B:
            print('Yes')
            a += 1
        else:
            print('No')
    else:
        if a+b<A+B and b<B:
            print('Yes')
            b += 1
        else:
            print('No')