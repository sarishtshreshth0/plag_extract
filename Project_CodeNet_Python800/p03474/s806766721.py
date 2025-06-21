#33 2020/07/14
A, B = input().split(' ')
A = int(A)
B = int(B)
S = input()
if not '-' in S:
  print('No')
else:
  S = S.split('-')
  if '-' in S[0] or '-' in S[1]:
    print('No')
  elif len(S[0]) == A and len(S[1]) == B:
    print('Yes')
  else:
    print('No')
