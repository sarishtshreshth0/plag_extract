n=int(input())
s=(input())

v=s[0]
count=1
for i in range(n):
  if s[i] == v:
    continue
  v = s[i]
  count += 1
print(count)