A, B=map(int,input().split())
 
func=lambda x:[x,x+13][x==1]
 
if func(A)==func(B):
  print('Draw')
elif func(A)<func(B):
  print('Bob')
else:
  print('Alice')