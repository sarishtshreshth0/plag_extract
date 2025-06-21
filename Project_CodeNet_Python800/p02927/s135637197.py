M, D = map(int, input().split())

count = 0

if M < 4 or D < 22:
  print(0)
else:
  for i in range(4,M+1):
    for j in range(22,D+1):
      d = list(str(j))
      if int(d[0]) < 2 or int(d[1]) < 2:
        continue
      if i == int(d[0])*int(d[1]):
        count += 1
      
    
  
  print(count)