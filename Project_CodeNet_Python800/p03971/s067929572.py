n, a, b = map(int, input().split())
s = input()
ans = []
x = 0
y = 0
for i in range(n):
  if s[i] == 'c':
    ans.append('No')
  elif s[i] == 'a':
    if x < a + b:
      x += 1
      ans.append('Yes')
    else:
      ans.append('No')
  elif s[i] == 'b':
    if x < a + b and y + 1 <= b:
      x += 1
      y += 1
      ans.append('Yes')
    else:
      ans.append('No')

for e in ans:
  print(e)   