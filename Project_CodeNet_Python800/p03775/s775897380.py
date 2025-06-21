from math import *
N=int(input())
K=sqrt(N)
F=11
for a in range(1,int(K)+1):
  if N%a==0:
    b=N//a
    al=len(str(a))
    bl=len(str(b))
    G=max(al,bl)
    F=min(F,G)
print(F)