a,b,c=map(int,input().split())
if c in list(range(min(a,b),max(a,b))):
  print('Yes')
else:
  print('No')