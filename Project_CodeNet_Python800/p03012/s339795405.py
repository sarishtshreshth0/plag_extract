n=int(input())
l=list(map(int,input().split()))
s=sum(l)
m=100000000
c=0
for i in range(n):
    c+=l[i]
    x=s-c
    d=abs(c-x)
    m=min(m,d)
print(m)
