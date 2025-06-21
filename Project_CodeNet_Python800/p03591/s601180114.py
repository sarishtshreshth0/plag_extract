S = input()
flag = False
if (len(S) < 4):
  flag = False
else:
  if (S[0] == 'Y' and S[1] == 'A' and S[2] == 'K' and S[3] == 'I'):
    flag = True
  
if flag:
  print('Yes')
else:
  print('No')