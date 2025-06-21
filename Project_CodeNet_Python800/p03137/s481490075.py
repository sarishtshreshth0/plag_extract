n,m = map(int,input().split())
x = list(map(int,input().split()))

if n >= m :
  print(0)
else:
  y = [0] * (m-1)
  x.sort()
  for i in range(1,m):
    y[i-1] = abs(x[i] - x[i-1])
  y.sort(reverse=True)
  print(sum(y[n-1:]))
