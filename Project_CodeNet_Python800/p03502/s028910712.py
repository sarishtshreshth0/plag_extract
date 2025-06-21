N = input()

X = 0

for i in range(len(N)):
  X = X + int(N[i])

if int(N)%X==0:
  print('Yes')
else:
  print('No')
