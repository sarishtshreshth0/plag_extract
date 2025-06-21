N=int(input())
A=list(map(int,input().split()))

S=[]
temp=0
for i in range(N):
    temp=temp+A[i]
    S.append(temp)

from collections import Counter

cnt=Counter(S)

ans=0
for c in cnt.values():
    ans+=c*(c-1)//2

if cnt[0]!=0:
    ans+=cnt[0]

print(ans)

