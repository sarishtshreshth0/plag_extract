M,D = map(int,input().split())
ans = 0
for d in range(22,D+1):
    s = str(d)
    if s[1]<"2":continue
    for m in range(1,M+1):
        if eval(s[0]+"*"+s[1])==m:
            ans+=1
print(ans)