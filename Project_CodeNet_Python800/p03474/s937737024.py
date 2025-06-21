A, B = map(int, input().split())
S = input()

if S[:A].isnumeric() and S[A] == "-" and S[A+1:A+B+1].isnumeric():
  print('Yes')
else:
  print('No')