n = int(input())
s = input()
b = s[0]
ans = 0
for i in range(1, n):
  if b == s[i]:
    next
  else:
    ans += 1
    b = s[i]
ans += 1
print(ans)