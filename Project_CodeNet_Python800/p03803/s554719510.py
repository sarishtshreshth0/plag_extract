a,b=[str(i) for i in input().split()]
list=["2","3","4","5","6","7","8","9","10","11","12","13","1"]
A=list.index(a)
B=list.index(b)
if A>B:
  print('Alice')
elif A==B:
  print('Draw')
else:
  print('Bob')