s=input()
o1=0
o0=0
e1=0
e0=0
for i in range(0,len(s),2):
  if s[i]=='1': o1+=1
  else: o0+=1
for i in range(1,len(s),2):
  if s[i]=='1': e1+=1
  else: e0+=1
if o1+e0<o0+e1: print(len(s)-(o0+e1))
else: print(len(s)-(o1+e0))