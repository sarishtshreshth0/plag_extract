N=int(input())
W=list(map(int,input().split()))
SUM=sum(W)
a=[]
b=[]
c=[]
for i in range (N):
    a.append(0)
for i in range (N):
    b.append(0)
for i in range (N):
    c.append(0)
for i in range(0,N):
    for j in range(0,i+1):
        a[i]=a[i]+W[j]
for i in range(0,N):
    b[i]=SUM-a[i]
for i in range(0,N):
    c[i]=abs(a[i]-b[i])
print(min(c))