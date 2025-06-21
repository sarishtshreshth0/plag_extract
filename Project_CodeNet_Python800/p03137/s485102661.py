n,m=map(int,input().split())
x=list(map(int,input().split()))
if n>=m:
    print(0)
else:
    y=[]
    x=sorted(x)
    for i in range(m-1):
        y.append(x[i+1]-x[i])
    ans=0
    y=sorted(y)
    for i in range(n-1):
        ans+=y[-i-1]
    print(sum(y)-ans)
        
    
