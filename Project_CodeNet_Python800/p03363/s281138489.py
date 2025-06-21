import sys,collections,itertools
input = sys.stdin.readline
N=int(input())
a=list(map(int,input().split()))
A =[0]+list(itertools.accumulate(a))
Ac = collections.Counter(A)
cnt = 0
for val in Ac.values():
    cnt += val*(val-1)//2
print(cnt)