Q, H, S, D = map(int, input().split())
N = int(input())

if H > Q*2:
  H = Q*2
if S > H*2:
  S = H*2
if D > S*2:
  D = S*2

if N % 2 == 0:
  print((N//2)*D)
else:
  print((N//2)*D+S)