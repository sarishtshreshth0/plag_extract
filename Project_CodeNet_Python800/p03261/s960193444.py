import collections
N=int(input())
W=[""]*N
for i in range(N):
  W[i]=input()
c=collections.Counter(W)
if len(c)!=N :
  print("No")
  exit()
for i in range(N-1):
  if W[i][-1] != W[i+1][0] :
    print("No")
    exit()
print("Yes")