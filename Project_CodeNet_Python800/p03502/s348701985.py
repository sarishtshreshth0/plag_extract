N=input()
if int(N)%sum([int(x) for x in N])==0:
  print('Yes')
else:
  print('No')