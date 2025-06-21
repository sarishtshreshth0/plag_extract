s = input()
n = len(s)
t = s[0]
ans = 0
for i in range(1,n):
  if i % 2 == 1:
    if t == s[i]:
      ans += 1
  else:
    if t != s[i]:
      ans += 1
print(ans)
