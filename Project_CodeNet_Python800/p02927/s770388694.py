m,d=map(int,input().split())


ans=0
if d<22:
    print(0)
    exit()
    
else:
    d1=int(str(d)[0])
    d2=int(str(d)[1])
    for i in range(2,10):
        for j in range(2,10):
            if i*j<=m and 10*i+j<=d and j!=1:
                ans+=1

print(ans)
