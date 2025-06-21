m, d = map(int, input().split())
count = 0
for i in range(1, m+1):
  for j in range(22, d+1):
    d1 = j % 10
    if d1 <= 1:
      continue
    d2 = int(j / 10)
    if d1 * d2 == i:
      count += 1
      #print(str(i) + " " + str(j))
print(count)