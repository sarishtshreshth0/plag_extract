n = int(input())
s = list(input())

ans = 1
temp = s[0]

for i in range(1,n):
    if temp != s[i]:
        ans += 1
        temp = s[i]

print(ans)
