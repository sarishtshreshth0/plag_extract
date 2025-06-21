m,d=map(int,input().split())
ans=0
if d<22:
    print(ans)
    exit()
for i in range(1,m+1):
    for j in range(22,d+1):
        if int(str(j)[-1])>=2:
            if i==int(str(j)[0])*int(str(j)[-1]):
                ans+=1
print(ans)