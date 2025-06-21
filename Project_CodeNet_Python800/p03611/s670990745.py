from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

ans = 0
amin = min(a)
amax = max(a)
for x in range(amin, amax+1):
   ans = max(ans, c[x-1]+c[x]+c[x+1])

print(ans)
