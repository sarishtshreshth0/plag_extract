from collections import Counter
N = int(input())
A = list(map(int, input().split()))
l = [0]
for i in range(N):
  l.append(l[-1]+A[i])
  
c = Counter(l)
ans = 0
for n in c.values():
  ans += n*(n-1)//2
print(ans)