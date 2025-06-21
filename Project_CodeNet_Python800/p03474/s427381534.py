x,y=map(int, input().split())
S=input()
if len(S)==x+y+1 and S[x]=='-' and S.count('-')==1:
  print('Yes')
else:
  print('No')