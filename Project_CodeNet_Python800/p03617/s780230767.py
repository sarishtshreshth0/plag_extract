Q,H,S,D=map(int,input().split())
N=int(input())
litre=min(4*Q,2*H,S)
Litre=min(2*litre,D)
if N%2==0:
  print(Litre*(N//2))
else:
  print(Litre*(N//2)+litre)