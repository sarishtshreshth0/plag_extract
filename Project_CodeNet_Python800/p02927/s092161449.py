M,D=map(int,input().split())

ans=0
for m in range(1,M+1):
    for d in range(10,D+1):
        d1,d10=d%10,d//10
        if d1*d10==m and d1>1 and d10>1:
            ans+=1
print(ans)