N=int(input())
L=list(map(int,input().split()))
R={}
sums=0
for i in range(N):
  sums+=L[i]
  if sums in R:
    R[sums]+=1
  else:
    R[sums]=1
k=0
if 0 in R:
  k=R[0]
print(sum([i*(i-1)//2 for i in R.values()])+k)