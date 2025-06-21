A, B = map(int, input().split())
S = list(input())
x = len(S)
if len(S) != A + B + 1:
  print('No')
if S[A] == '-' :
  if S.count('-') == 1:
  
    print('Yes')
  else:
    print('No')
else:
  print('No')