n = int(input())
a = [int(i) for i in input().split()]
for i in range(n-1):
  a[i+1] += a[i]
  
from collections import Counter
c = Counter(a)
ans = c[0]
for i,v in c.items():
  ans += v*(v-1)//2
  
print(ans)