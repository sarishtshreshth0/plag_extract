M,D=map(int,input().split())

ans=0
i=1
while i<=M:
    j=22
    while j<=D:
        if j%10>=2 and (j//10)*(j%10)==i:
            ans+=1
        j+=1
    i+=1
print(ans)