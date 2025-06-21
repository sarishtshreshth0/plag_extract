(n,),*d=[list(map(int,c.split()))for c in open(0)]
for i in range(n-1):
 t=0
 for j in range(i,n-1):c,s,f=d[j];t=[t+(f-t%f)%f,s][t<s]+c
 print(t)
print(0)