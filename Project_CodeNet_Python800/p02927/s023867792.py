m,d=map(int,input().split())
cnt=0
for i in range(1,m+1):
    for j in range(22,d+1):
        d10=j//10
        d1=j%10
        if i==d10*d1 and d1>=2:
            cnt+=1
print(cnt)