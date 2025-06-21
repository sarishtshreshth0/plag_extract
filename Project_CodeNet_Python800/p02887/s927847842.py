n= int(input())
s = input()
ans = 1
prev = s[0]
for i in range(n-1):
    if prev==s[i+1]:
        pass
    else:
        ans += 1
        prev = s[i + 1]

print(ans)