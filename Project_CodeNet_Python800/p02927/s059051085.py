m,d=map(int,input().split())
ans=0
if m>=4 and d>=22:
    for i in range(4,m+1):
        for j in range(22,d+1):
            d2=j//10
            d1=j%10
            if d2>=2 and d1>=2 and d2*d1==i:
                ans+=1
print(ans)