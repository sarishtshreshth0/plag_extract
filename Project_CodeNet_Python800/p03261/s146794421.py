n = int(input())
che = [input()]
for i in range(1,n):
  a = input()
  if a in che:
    print('No')
    exit()
  else:
    che.append(a)
    if che[i-1][-1] == che[i][0]:
      continue
    else:
      print('No')
      exit()
print('Yes') 