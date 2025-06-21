Score_Alice, Score_Bob = map(int, input().split())

if Score_Alice == 1 and Score_Bob == 1:
  print('Draw')
elif Score_Alice == 1 and Score_Bob != 1:
  print('Alice')
elif Score_Alice != 1 and Score_Bob == 1:
  print('Bob')
else:
  if Score_Alice > Score_Bob:
    print('Alice')
  elif Score_Alice < Score_Bob:
    print('Bob')
  else:
    print('Draw')