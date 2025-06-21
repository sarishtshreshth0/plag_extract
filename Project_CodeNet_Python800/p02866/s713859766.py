import sys,math,collections,itertools
input = sys.stdin.readline
m=998244353

N=int(input())
D=list(map(int,input().split()))
Dc = collections.Counter(D)
count=1
if D[0] !=0 or Dc[0]>1:
    print(0)
else:
    for i in range(1,max(Dc.keys())+1):
        count *=pow(Dc[i-1],Dc[i],m)
    print(count%m)
    
