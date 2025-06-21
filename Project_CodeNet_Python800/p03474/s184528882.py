A,B=map(int,input().split(' '))
S=input()
if S[A] == '-' and all(c in '0123456789' for c in S[:A]) and all(c in '0123456789' for c in S[A+1:]):
  print('Yes')
else:
  print('No')