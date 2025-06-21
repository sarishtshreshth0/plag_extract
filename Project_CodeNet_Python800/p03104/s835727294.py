A,B=list(map(int, input().split()))
if A==B:
  print(A)
  exit()
a=A//4
b=B//4

def xorsum(L):
  if len(L)==1:
    return L[0]
  a=L[0]
  for i in range(1,len(L)):
    a^=L[i]
  return a

if a==b:
  L=[A+i for i in range(B-A+1)]
  print(xorsum(L))
  exit()
c=[a*4+i for i in range(4) if i>=A%4]
d=[b*4+i for i in range(4) if i<=B%4]
print(xorsum(c)^xorsum(d))