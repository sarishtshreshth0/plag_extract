import copy
def change(k):
  if k==0:
    return int(1)
  else:
    return int(0)
t=0
m=0
S=list(map(int,list(input())))
M=copy.copy(S)
T=copy.copy(S)
N=len(S)
for i in range(N):
  if i==0:
    if T[i]==0:
      t+=1
      T[0]=1
    else:
      m+=1
      M[0]=0
  else:
    if T[i]==T[i-1]:
      T[i]=change(T[i])
      t+=1
    if M[i]==M[i-1]:
      M[i]=change(M[i])
      m+=1
print(min(t,m))