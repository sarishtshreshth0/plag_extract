n,a,b=map(int,input().split())
s=input().strip()
njp=0
nop=0
for i in range(len(s)):
  if s[i]=='a':
    if njp<(a+b):
      njp+=1
      print('Yes')
    else:
      print('No')
  elif s[i]=='b':
    if njp<(a+b):
      if nop<b:
        nop+=1
        njp+=1
        print('Yes')
      else:
        print('No')
    else:
      print('No')
  else:
    print('No')
