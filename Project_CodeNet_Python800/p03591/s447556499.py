s = input()
if len(s) < 4:
  print('No')
else:
  t = s[:4]
  if t == 'YAKI':
    print('Yes')
  else:
    print('No')