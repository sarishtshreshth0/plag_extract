month,day = map(int,input().split())

if day < 22:
  print(0)
else:
  s = 0
  for j in range(month+1):
    for i in range(22,day+1):
      num_1 = i%10
      num_2 = (i-num_1)/10
      if  num_1< 2:
        continue
      elif num_1 * num_2 == j:
        s += 1
  print(s)