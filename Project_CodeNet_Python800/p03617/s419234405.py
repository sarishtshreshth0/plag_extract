Q, H, S, D = [int(x) for x in input().strip().split()]
N = int(input())
min_QHS = min(Q * 4, H * 2, S)
if min_QHS * 2 <= D:
  print(N * min_QHS)
else:
  print(D * (N // 2) + (N % 2) * min_QHS)