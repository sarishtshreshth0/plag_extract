Q,H,S,D = map(int, input().split())
N = int(input())

if N % 2 == 0:
  print(min(Q*N*4,H*N*2,S*N,D*N//2))
else:
  N -= 1
  print(min(Q*N*4,H*N*2,S*N,D*N//2) + min(Q*4,H*2,S))