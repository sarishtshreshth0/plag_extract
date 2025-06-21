m,d=map(int,input().split())
ans=0
for month in range(1,m+1):
    for day in range(1,d+1):
        day=str(day)
        if len(day)!=2:
            continue
        if int(day[0])*int(day[1])!=month:
            continue
        if int(day[0])<2 or int(day[1])<2:
            continue
        #print(month,day)
        ans+=1
print(ans)