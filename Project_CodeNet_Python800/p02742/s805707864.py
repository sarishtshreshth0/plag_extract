N, M = map(int, input().split())

if N == 1 or M == 1:
  print(1)
elif N*M % 2 == 0:
  print(N*M//2)
else:
  print(N*M//2 + 1)
