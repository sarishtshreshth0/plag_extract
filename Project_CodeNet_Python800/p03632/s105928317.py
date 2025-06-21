A, B, C, D = map(int,input().split())

count = 0

for i in range(101):
  if A<=i and i<=B and C<=i and i<=D:
    count = count + 1

if count!=0:
  count = count - 1

print(count)
