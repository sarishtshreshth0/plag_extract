from collections import Counter
mod=998244353
n=int(input())
D=list(map(int,input().split()))
Count=Counter(D)
if D[0]!=0 or Count[0]!=1:print(0);exit()

ans=1
for i in range(1,max(D)+1):
    ans *=Count[i-1]**Count[i]
    ans %=mod
print(ans)