n,d=map(int,input().split())
x= [list(map(int, input().split())) for i in range(n)]
lis=list(i**2 for i in range(0,128))
ans=0
for i in range(n):
    for k in range(i+1,n):
        check=0
        for j in range(d):
            check+=(x[i][j]-x[k][j])**2
        if check in lis:
            ans+=1
print(ans)