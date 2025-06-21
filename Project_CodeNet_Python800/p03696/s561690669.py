_,s=input(),input()
t=0
for c in s:
  if c=='(': t+=1
  else: t-=1
  if t<0: s='('+s; t+=1
print(s+')'*t)