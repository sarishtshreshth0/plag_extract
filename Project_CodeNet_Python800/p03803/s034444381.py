A, B = map(int, input().split())
if (A-2)%13 > (B-2)%13:
  print('Alice')
elif (A-2)%13 < (B-2)%13:
  print('Bob')
else:
  print('Draw')