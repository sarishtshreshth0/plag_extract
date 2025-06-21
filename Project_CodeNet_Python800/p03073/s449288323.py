s = input()
ans = 0

for i in range(1, len(s)):
  if s[i-1] == s[i]:
    if s[i] == '0':
      s = s[:i] + '1' + s[i+1:]
      ans += 1
    else:
      s = s[:i] + '0' + s[i+1:]
      ans += 1

print(ans)    