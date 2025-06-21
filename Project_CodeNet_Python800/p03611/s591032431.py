from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
ans = 0
for x in range(min(a), max(a)+1):
  res = c[x] + c[x+1] + c[x-1]
  ans = max(ans, res)
print(ans)