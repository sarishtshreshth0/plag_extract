#a以上のbの倍数の最小値
def baisu(a,b):
  if a%b==0:
    return a
  else:
    return ((a//b)+1)*b
C=list()
S=list()
F=list()
N=int(input())
for i in range(N-1):
  c,s,f=map(int,input().split())
  C.append(c)
  S.append(s)
  F.append(f)
L = [[0 for j in range(N)] for i in range(N)]
for i in range(N-1):
  L[i][i]=S[i]
  for j in range(i+1,N):
    L[i][j]=baisu(max(L[i][j-1],S[j-1]),F[j-1])+C[j-1]
  print(L[i][-1])
print(0)