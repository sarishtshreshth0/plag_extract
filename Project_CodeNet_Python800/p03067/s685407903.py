a,b,c=map(int,input().rstrip().split(' '))
if (a<c<b) or (b<c<a):
  print('Yes')
else:
  print('No')
