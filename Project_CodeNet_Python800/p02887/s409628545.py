n = int(input())
s = input()
prev = ""
ans = ""
for i in range(n):
    if s[i] == prev:
        continue
    prev = s[i]
    ans += s[i]
print(len(ans))