s=0
A,B=map(int,input().split())
if abs(A-B)<30:
  for i in range(A,B+1):
    s=s^i
  print(s)
else:
  c=A//4
  L=range(A,4*(c+1))
  for i in L:
    s=s^i
  c=B//4
  L=range(4*(c-1),B+1)
  for i in L:
    s=s^i
  print(s)