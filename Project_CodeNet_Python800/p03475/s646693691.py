n = int(input())
c, s, f = [], [], []
for i in range(n-1):
  i, j, k = map(int, input().split())
  c.append(i)
  s.append(j)
  f.append(k)

for i in range(n - 1):
  time = s[i] + c[i]
  i += 1
  while i < n - 1:
    if time < s[i]:
      time = s[i] + c[i]
    else:
      time += (f[i] - (time - s[i]) % f[i]) % f[i] + c[i]
    i += 1
  print(time)

print(0)