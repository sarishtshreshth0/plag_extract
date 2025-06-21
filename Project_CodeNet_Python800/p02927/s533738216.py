M,D = map(int,input().split())

ans = 0
for m in range(1,M+1):
    for d in range(10,D+1):
        a,b = map(int,str(d))
        if a>=2 and b>=2 and a*b == m:
            ans += 1
print(ans)