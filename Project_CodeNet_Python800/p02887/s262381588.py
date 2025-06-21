input()
s=input()
t,a=s[0],1
for c in s:
  if c!=t: a+=1; t=c
print(a)