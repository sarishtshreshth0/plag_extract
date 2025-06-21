N, K = map(int, input().split())
r = 1
while not(K**(r-1) <= N and N < K ** r):
  r += 1
print(r)