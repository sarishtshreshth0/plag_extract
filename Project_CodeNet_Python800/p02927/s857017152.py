M, D = map(int, input().split())
count = 0
if D >= 22:
  for i in range(22, D + 1):
    j = str(i)
    if int(j[1]) >= 2:
      m = int(j[0]) * int(j[1])
      if m <= M:
        count += 1
print(count)