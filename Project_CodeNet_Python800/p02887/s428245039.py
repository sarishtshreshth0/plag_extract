n = int(input())
s = str(input())
s_new = s[0]

for i in range(1,len(s)):
  if s_new[-1] != s[i]:
    s_new = s_new + s[i]

print(len(s_new))