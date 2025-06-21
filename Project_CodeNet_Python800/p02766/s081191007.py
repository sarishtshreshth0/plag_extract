N, K = map(int, input().split())
c = 1
while N//K != 0:
  N = N//K
  c += 1
print(c)