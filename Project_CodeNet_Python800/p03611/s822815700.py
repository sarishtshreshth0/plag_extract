import collections
N=int(input())
a=list(map(int,input().split()))

for i in range(N):
    a.append(a[i]-1)
    a.append(a[i]+1)

cc=collections.Counter(a)
ans=max(list(cc.values()))

print(ans)