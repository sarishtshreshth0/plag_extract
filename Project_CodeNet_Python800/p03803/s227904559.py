A,B = (int(x) for x in input().split())
if A == B:
  print ('Draw')
elif A > B:
  if A == 13 and B == 1:
    print ('Bob')
  else:
    print ('Alice')
else:
  if A == 1 and B == 13:
    print ('Alice')
  else:
    print ('Bob')