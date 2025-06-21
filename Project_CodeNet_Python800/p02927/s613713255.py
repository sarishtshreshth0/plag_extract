m,d=map(int,input().split())

ans=0
for i in range(1,m+1):
    for j in range(22,d+1):
        if int(str(j)[1])>=2 and int(str(j)[0])*int(str(j)[1])==i:
            ans+=1
            # print(i,j)
print(ans)
