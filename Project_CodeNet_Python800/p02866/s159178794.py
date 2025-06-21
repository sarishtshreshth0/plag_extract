N,D=open(0)
*D,=map(int,D.split())
c=[0]*-~max(D)
for i in D:c[i]+=1
a=D[0]<1==c[0]
for i,j in zip(c,c[1:]):a*=i**j
print(a%998244353)
