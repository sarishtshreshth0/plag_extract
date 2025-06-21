M,D=[int(i) for i in input().split()]

if D<20:
  print(0)
else :
  count = 0
  for i in range(1,M+1):
    for id in list(range(20, D+1)):
      if int((str(id))[1]) >= 2 and ( int(str(id)[0]))*int((str(id))[1]) == i :
         count += 1
  print(count)
