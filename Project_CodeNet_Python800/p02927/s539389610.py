m, d = map(int, input().split())
c = 0
for i in range(22, d+1):
  if i//10>=2 and i%10>=2 and (i//10) * (i%10) <= m:
    c += 1
print(c)