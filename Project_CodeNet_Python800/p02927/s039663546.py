m,d=map(int,input().split())
cnt=0
for i in range(1,m+1):
    for j in range(1,d+1):
        da=j%10
        db=j//10
        if da>=2 and db>=2:
            if i==da*db:
                cnt+=1
print(cnt)