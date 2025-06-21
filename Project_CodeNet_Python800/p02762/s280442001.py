n,m,k=map(int,input().split())
BAD=[0 for i in range(n+1)]

E=[]
for inp in range(m):
    a,b=map(int,input().split())
    E.append((a,b))
    BAD[a]-=1
    BAD[b]-=1

B=[] 
for inp in range(k):
    a,b=map(int,input().split())
    B.append((a,b))
    
uf=[i for i in range(n+1)]
def uf_find(x,uf=uf):
    while uf[x]!=x:
        x=uf[x]
    return x       


res=[]

for ele in E:
    if uf_find(ele[0]) == uf_find(ele[1]):
        continue
    else:
        res.append((ele[0],ele[1])) #write result
        
        if uf_find(ele[0])>uf_find(ele[1]):
            uf[uf_find(ele[0])]=uf_find(ele[1])
        else:
            uf[uf_find(ele[1])]=uf_find(ele[0])

SCO=[0 for i in range(n+1)]
for i in range(1,n+1):
    SCO[uf_find(i)]+=1


for bl in B:
    if uf_find(bl[0])==uf_find(bl[1]):
        BAD[bl[0]]-=1
        BAD[bl[1]]-=1

ANS=[str(SCO[uf_find(i)] + BAD[i] -1) for i in range(1,n+1)]
print(" ".join(ANS))
        
