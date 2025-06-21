n,d=map(int,input().split())
x=[[int(i) for i in input().split()] for j in range(n)]
ans=0
for i in range(n):
    for j in range(n-1,0,-1):
        if j==i:
            break
        s=0
        for k in range(d):
            s+=(x[i][k]-x[j][k])**2
        
        s=s**0.5
        if int(s)==s:
            ans+=1
print(ans)