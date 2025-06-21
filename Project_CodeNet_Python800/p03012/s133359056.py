n=int(input())
bop=list(map(int,input().split()))
hq=sum(bop)

for i in range(1,n):
  		hq=min(hq, abs(sum(bop[:i])-sum(bop[i:n])))

print(hq)