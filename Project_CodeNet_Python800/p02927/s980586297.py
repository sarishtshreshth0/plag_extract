m, d = map(int, input().split())
if d < 22:
  print(0)
  exit()
cnt = 0
for i in range(1, m + 1):
  for j in range(22, d + 1):
    ten = int(str(j)[0])
    one = int(str(j)[1])
    if ten >= 2 and one >= 2 and ten * one == i:
      cnt += 1
print(cnt)