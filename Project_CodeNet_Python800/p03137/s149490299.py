n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
if n>=m:
    print(0)
else:
    s=[]
    for i in range(m-1):
        a=x[i+1]-x[i]
        s.append(a)
    s.sort()
    ans=0
    for i in range(m-n):
        ans+=s[i]
    print(ans)