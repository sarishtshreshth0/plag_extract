a,b=map(int,input().split())
s=input()
han=0
for i in range(a):
  if s[i].isdecimal() ==False:
    han +=1
    
for i in range(a+1,a+b+1):
  if s[i].isdecimal() ==False:
    han +=1
if s[a]!='-':
  han +=1

if han ==0:
  print('Yes')
else:
  print('No')