*s, t = map(int, input().split())
s.sort()
f = False
for i in range(s[0],s[1]+1):
  if i == t:
    f = True
print("Yes") if f else print("No")