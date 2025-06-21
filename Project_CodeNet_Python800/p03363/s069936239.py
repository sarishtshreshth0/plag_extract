N = int(input())
A = list(map(int, input().split()))
d = {}
x = 0
for i in range(N):
  x += A[i]
  d[x] = d.get(x, 0) + 1
ans = d.get(0, 0)
for x in d.values():
  ans += x * (x-1) // 2
print(ans)