from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
ans=0

d=defaultdict(int)
sum_a=0
d[sum_a]+=1
for i in range(n):
    sum_a+=a[i]
    ans+=d[sum_a]
    d[sum_a]+=1
print(ans)