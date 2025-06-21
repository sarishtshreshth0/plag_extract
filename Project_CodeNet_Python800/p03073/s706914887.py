s = input()
x = 0
y = 0
for i in range(len(s)):
  if i % 2 != int(s[i]):
    x += 1
for j in range(len(s)):
  if j % 2 == int(s[j]):
    y += 1
print(min(x, y))