a,b,c=map(int,input().split())
if c in range(a,b+1) or c in range(b+1,a):
  print('Yes')
else:
  print('No')