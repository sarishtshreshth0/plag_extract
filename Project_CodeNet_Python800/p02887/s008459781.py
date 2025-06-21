n = int(input())
s = input()

ans = 1
prev = s[0]
for i in range(1, len(s)):
    if s[i] == prev:
        continue
    ans += 1
    prev = s[i]
print(ans)
