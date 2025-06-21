n,a,b=map(int,input().split())
c=d=1
e=0
m=10**9+7
for i in range(1,b+1):
    c=(c*(n+1-i))%m
    d=(d*i)%m
    if i==a or i==b:
        e+=c*pow(d,m-2,m)%m
print((pow(2,n,m)-e-1)%m)