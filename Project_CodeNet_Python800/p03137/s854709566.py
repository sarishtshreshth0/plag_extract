n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= m:
  print(0)
  exit()

d = [0] * (m-1)
x.sort()

for i in range(m-1):
  d[i] = x[i+1] - x[i]
d.sort(reverse=True)
mx = x[-1] - x[0]
r = n - 1
dsum = sum(d[:r])
print(mx - dsum)