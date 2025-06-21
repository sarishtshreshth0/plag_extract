m,d=map(int,input().split())
ans=0
for i in range(1,m+1):
    for j in range(20,d+1):
        x=str(j)
        if int(x[1])>=2:
            if int(x[0])*int(x[1])==i:
                ans+=1
print(ans)
