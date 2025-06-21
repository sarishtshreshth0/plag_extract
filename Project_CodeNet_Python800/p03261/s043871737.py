import sys
N=int(input())
S=input()
L=list()
m=S[-1]
L.append(S)
for i in range(N-1):
  S=input()
  if S[0]!=m:
    print("No")
    sys.exit()
  else:
    L.append(S)
    m=S[-1]
if len(set(L))==N:
  print("Yes")
else:
  print("No")