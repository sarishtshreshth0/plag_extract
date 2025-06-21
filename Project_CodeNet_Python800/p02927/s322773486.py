m, d = map(int, input().split(' '))

cnt = 0
if d < 22:
  print(0)
else:
  for i in range(22,d + 1):
    d10 = i // 10
    d1 = i % 10
    if d10 >= 2 and d1 >= 2 and d10*d1 <= m:
      cnt += 1
      
  print(cnt)