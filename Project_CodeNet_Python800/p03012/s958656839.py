N = int(input())
W = [int(x) for x in input().split()]
res = 1000
for i in range(1,N-1):
  r = W[0:i+1]
  l = W[i+1:N]
  R = sum(r)
  L = sum(l)
  a = abs(R-L)
  if a < res:
    res = a
print(res)