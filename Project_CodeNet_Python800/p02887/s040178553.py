a = int(input())
s = input()
ans = ''
for i in range(a-1):
    if s[i] == s[i+1]:
        continue
    else:
        ans += s[i]
ans += s[-1]
#print(ans)
print(len(ans))