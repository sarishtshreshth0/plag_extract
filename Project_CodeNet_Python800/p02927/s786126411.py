m,d = map(int,input().split())

ans=0
for i in range(1,m+1):
    for j in range(1,d+1):
        if j >= 10:
            d10=int(str(j)[0])
            d1=int(str(j)[1])
            if d1 >= 2 and d10 >= 2 and d1*d10==i:
                ans+=1

print(ans)