import sys
n,m=map(int,input().split())
x =list(map(int,input().split()))

ans=0
if n>=m:
    ans=0
else:
    x.sort()
    diff=[0]*(m-1)

    for i in range(m-1):
        diff[i]=x[i+1]-x[i]

    diff.sort()

    ans=0
    
    for i in range(m-n):
        ans+=diff[i]

print(ans)
