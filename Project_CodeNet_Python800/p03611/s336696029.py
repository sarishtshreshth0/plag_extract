from collections import Counter
N = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(N):
  n = a[i]
  ans.append(n-1)
  ans.append(n)
  ans.append(n+1)
  
c = Counter(ans)
m = c.most_common()
print(m[0][1])