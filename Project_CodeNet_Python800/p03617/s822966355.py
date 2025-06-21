Q,H,S,D = map(int,input().split())
N = int(input())

S = min(S,2*H,4*Q)
if N != 1:
  if 2*S <= D:
    print(S*N)
  else:
    print(D*(N//2) +(N%2)*S)
else:
  print(S)