a,b = map(int,input().split())
L = list(range(2,14))+[1]
if L.index(a) > L.index(b):
  print('Alice')
elif L.index(a) == L.index(b):
  print('Draw')
else:
  print('Bob')