n,d = map(int,input().split())

X=[]
for i in range(n):
    x=list(map(int,input().split()))
    X.append(x)

c=0
D2=[]
for i in range(n-1):
    for j in range(i+1,n):
        d2=0.0
        for k in range(d):
            d2 += (X[i][k]-X[j][k])**2
        D2.append(d2**0.5)
        if (d2**0.5)%1==0 :
            c+=1
print(c)
