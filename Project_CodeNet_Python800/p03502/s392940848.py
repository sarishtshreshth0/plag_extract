N = input()
total = 0
for i in N:
  total += int(i)
if int(N)%total ==0:
  print('Yes')
else:
  print('No')