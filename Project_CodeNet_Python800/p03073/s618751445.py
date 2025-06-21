s=input()
a=[]
for i in range(0,len(s)//2*2,2):
  a.append(s[i:i+2])
a10=a.count('10')
a01=a.count('01')

if len(s)%2:
  s1=int(s[-1])
else:s1=-1

if a10>a01:
  if s1==0:
    cnt=len(a)-a10+a01+1
  else:
    cnt=len(a)-a10+a01
elif a01>a10:
  if s1==1:
    cnt=len(a)-a01+a10+1
  else:
    cnt=len(a)-a01+a10
else:
  cnt=len(a)
print(cnt)
