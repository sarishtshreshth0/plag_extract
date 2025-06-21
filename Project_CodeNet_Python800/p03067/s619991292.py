a,b,c=map(int,input().split())
a,b = min(a,b),max(a,b)
if c in range(a,b+1):
  print('Yes')
else:
  print('No')