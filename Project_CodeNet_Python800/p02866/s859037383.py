n=int(input())
a=list(map(int,input().split()))
if a[0]:
    print(0)
    exit()
a.sort()
j=0
l=list()
#print(a)
for i in range(max(a)+1):
    k=0
    while j<n and a[j]==i:
        j+=1
        k+=1
        #print(l,j,k)
    l.append(k)
#print(l)
p=l[0]==1
mod=998244353
for i in range(len(l)-1):
    #print(p)
    p=(p*pow(l[i],l[i+1],mod))%mod
print(p%mod)