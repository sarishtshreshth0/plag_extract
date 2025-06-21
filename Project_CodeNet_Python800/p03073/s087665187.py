s = list(input())
n = len(s)
for j in range(n):
  s[j] = int(s[j])
a = 0
b = 0

for i in range(n):
  if i%2 == 0 and s[i] == 0:
    a += 1
  elif i%2 == 0 and s[i] == 1:
    b += 1
  elif i%2 == 1 and s[i] == 0:
    b += 1
  else:
    a += 1
print(min(a,b))
