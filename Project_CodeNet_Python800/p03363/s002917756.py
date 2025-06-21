import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))
A =[0]
for i in range(N):
    A.append(A[-1]+a[i])

Ac = collections.Counter(A)
cnt = 0
for val in Ac.values():
    cnt += val*(val-1)//2
print(cnt)
