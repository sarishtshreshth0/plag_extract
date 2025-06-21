from collections import Counter
n = int(input())
a = list(map(int, input().split()))
A = [0]
for i in range(n):
  A.append(A[-1]+a[i])
A = Counter(A)
ans = 0
for x,y in A.items():
  if y >= 2: ans += (y-1)*y//2
print(ans)