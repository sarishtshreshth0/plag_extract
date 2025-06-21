A,B=map(int,input().split())
if A==1 or B==1:
  if A==B:
    print('Draw')
    exit()
  else:
    if A==1:
      print('Alice')
      exit()
    else:
      print('Bob')
      exit()
if A>B:
  print('Alice')
elif A==B:
  print('Draw')
else:
  print('Bob')