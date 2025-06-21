a,b=map(int, input().split())
if (a-2)%13 > (b-2)%13 :
  print('Alice')
elif (a-2)%13 == (b-2)%13 :
  print('Draw')
else:
  print('Bob')