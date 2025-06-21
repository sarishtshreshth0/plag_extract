n=int(input())
x=[list(map(int,input().split())) for i in range(n-1)]
for i in range(n):
    ans=0
    for j in range(i,n-1):
        if ans%x[j][2]==0:
            a=0
        else:
            a=x[j][2]-(ans%x[j][2])
        ans=(max(ans+a,x[j][1]))
        ans+=x[j][0]
    print(ans)