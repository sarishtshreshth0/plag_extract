n,m=map(int,input().split())
x=list(map(int,input().split()))
if n>=m:
    print(0)
    exit()

x=sorted(x)
l=[0]*(m-1)
for i in range(m-1):
    l[i]=x[i+1]-x[i]
    
l=sorted(l)[::-1]
dist=x[m-1]-x[0]-sum(l[:n-1])
print(dist)