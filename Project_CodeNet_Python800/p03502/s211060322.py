N = input()
if int(N)%sum(int(i) for i in N):
  print('No')
else:
  print('Yes')