M,D=map(int,input().split())
ans=0
for i in range(1,M+1):
    for j in range(1,D+1):
        m=i
        d=j
        s=str(d)
        if len(s)<2:
            continue
        d1=int(s[0])
        d2=int(s[1])
        if d1>1:
            if d2>1:
                if d1*d2==m:
                    ans+=1
print(ans)