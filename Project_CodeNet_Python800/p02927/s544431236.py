M,D=map(int,input().split())

if D<=21:
    print(0)
    exit()
ans=0
for i in range(4,M+1):
    for j in range(22,D+1):
        D1=int(str(j)[0])
        D2=int(str(j)[1])
        if i==D1*D2 and D1!=1 and D2!=1:
            ans+=1
            
print(ans)