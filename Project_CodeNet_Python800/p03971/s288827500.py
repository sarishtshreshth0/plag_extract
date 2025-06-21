N,A,B = map(int,input().split())
S = input()
SS = list(S)
CA = 0
CB = 0
for i in range(len(SS)):
  if SS[i] =='a':
    if CA < A+B:
      CA +=1
      print('Yes')
    else:
      print('No')
  elif SS[i] == 'b':
    CB += 1
    if CA < A+B and CB <= B :
      CA +=1
      print('Yes')
    else:
      print('No')
  else:
    print('No')