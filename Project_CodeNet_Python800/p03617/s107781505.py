Q,H,S,D=map(int,input().split())
Q*=4
H*=2
a=Q*2
b=H*2
c=S*2
d=D
s=min([a,b,c,d])
p=int(input())
if p%2==0:
  print(((p//2)*s))
else:
  print((p//2)*s+min([Q,H,S]))