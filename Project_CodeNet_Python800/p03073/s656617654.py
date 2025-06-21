s = input()
N = len(s)
f = s[0]
c = 0
for i in range(1,N):
  if i % 2 == 1:
    if f == s[i]:
      c+=1
  else:
    if f != s[i]:
      c+=1
print(c)