s = input()
s = list(s)
ans = 0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        if s[i+1]=="0":
            s[i+1] = "1"
        elif s[i+1]=="1":
            s[i+1] = "0"
        ans += 1
print(ans)
