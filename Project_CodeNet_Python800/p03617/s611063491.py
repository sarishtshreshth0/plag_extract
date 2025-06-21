Q, H, S, D = map(int, input().split())
M = min(2 * Q, H)
# 0.5,1,2
N = int(input())

if N % 2 == 0:
  print(min(M * 2 * N, S * N, D * N // 2))
else:
  print(min((M * 2 * (N-1)) + M * 2, S * (N-1) + S, D * (N-1) // 2 + M * 2, D * (N-1) // 2 + S))