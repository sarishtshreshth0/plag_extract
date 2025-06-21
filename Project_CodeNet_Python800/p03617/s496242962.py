Q,S,H,D = map(int,input().split())
N = int(input())

one = min(Q*4,S*2,H)

if one * 2 <= D:
  print(N * one)
else:
  if N % 2 == 0:
    print((N//2)*D)
  else:
    print((N//2)* D + one)