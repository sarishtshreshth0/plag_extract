n,a,b=map(int,input().split())
ab=a+b
S=input()
allp=0
forp=0
for s in S:
  if s=='a':
    if allp<ab:
      allp+=1
      print('Yes')
    else:
      print('No')
  elif s=='b':
    if allp<ab and forp<b:
      allp+=1
      forp+=1
      print('Yes')
    else:
      print('No')
  else:
    print('No')