n = int(input())
a = list(map(int,input().split()))
r = [0]*(n+1)
for i in range(n):
    r[i+1] = r[i]+a[i]
ans = r.count(0)-1
from collections import Counter
c = Counter(r[1:])
for i in c:
    ans += c[i]*(c[i]-1)//2
print(ans)