n,a,b=map(int,input().split())
s=input()
c=0
d=0
for i in range(n):
  if s[i]=='a':
    if c+d<a+b:
      print('Yes')
      c+=1
    else:
      print('No')
  elif s[i]=='b':
    if c+d<a+b and d<b:
      print('Yes')
      d+=1
    else:
      print('No')
  else:
    print('No')