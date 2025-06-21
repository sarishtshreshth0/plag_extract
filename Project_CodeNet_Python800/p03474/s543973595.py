import sys

A,B=map(int,input().split())
S=input()
if S[A]!='-':
  print('No')
  sys.exit()

try:
  int(S[:A])
  int(S[A+1:])
except:
  print('No')
  sys.exit()
print('Yes')