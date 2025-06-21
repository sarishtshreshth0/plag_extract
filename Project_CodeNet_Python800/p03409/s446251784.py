N=int(input())
R=sorted([list(map(int,input().split())) for i in range(N)])
B=sorted([list(map(int,input().split())) for i in range(N)])
U=[0]*N

for c,d in B:
  i,mv,mi=0,-1,0
  for i,(a,b) in enumerate(R):
    if a<c:
      if b<d and U[i]==0 and mv<b:
        mv,mi=b,i
    else:
      break
  if mv!=-1:
    U[mi]=1

print(sum(U))
