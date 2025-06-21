n,k=map(int,input().split())
xx=k
c=0
while xx<=n:
  xx=k**c
  c+=1
if c<1:
  c=2
print(c-1)