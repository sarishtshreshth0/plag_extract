N, K = map(int, input().split())

M = 0
i = 0

while M < N:
  M += (K-1)*K**i
  i += 1
print(i)