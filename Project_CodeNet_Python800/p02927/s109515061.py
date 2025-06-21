m,d= map(int, input().split())

ans=0
for mon in range(1,m+1):
    for day in range(1,d+1):
        if day<22:
            continue
        d1,d2=str(day)
        d1,d2=int(d1),int(d2)
        if d1<2 or d2<2:
            continue
        if d1*d2==mon:
            ans+=1

print(ans)