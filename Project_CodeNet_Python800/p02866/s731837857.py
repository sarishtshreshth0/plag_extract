N,*D=map(int,open(0).read().split())
c=[0]*N
for i in D:c[i]+=1
m=max(D)
if D[0]>0 or c[0]>1:print(0);exit()
a=1
for i in range(m):a*=c[i]**c[i+1]
print(a%998244353)
