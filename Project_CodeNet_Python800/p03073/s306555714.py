s=input()
ans=[0,0]
for i in range(len(s)):
    now=int(s[i])
    ans[0]+=now^0^(i%2)
    ans[1]+=now^1^(i%2)
print(min(ans))