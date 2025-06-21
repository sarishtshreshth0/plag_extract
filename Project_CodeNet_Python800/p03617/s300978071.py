Q,H,S,D=map(int, input().split())
N=int(input())
a=min(8*Q,4*H,2*S,D)
b=min(4*Q,2*H,S)
if N%2==0:
  print(a*(N//2))
else:
  print(a*(N//2)+b)