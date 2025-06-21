M, D= map(int, input().split())

ans = 0
for m in range(1, M+1):
    for d in range(22, D+1):
        s = str(d)
        if int(s[0])<2 or int(s[1])<2: continue
        if int(s[0])*int(s[1])==m:
            ans += 1

print(ans)
