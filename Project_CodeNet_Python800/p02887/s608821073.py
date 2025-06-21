n = int(input())
s = input()

s = s + '@'
prev = s[0]
ans = 0
for i in range(1, n + 1):
    if s[i] != prev:
        ans += 1
    prev = s[i]
print(ans)
