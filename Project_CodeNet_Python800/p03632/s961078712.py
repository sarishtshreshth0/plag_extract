A,B,C,D = map(int,input().split())
N = min(B,D)-max(A,C)
if N <= 0:
  print(0)
else:
  print(N)