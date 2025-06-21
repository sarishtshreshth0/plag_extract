S=input()
a1=0
a2=0
p1='1'
p2='0'
for s in S:
  if s!=p1:
    a1+=1
  else:
    a2+=1
  p=p1
  p1=p2
  p2=p
print(min(a1,a2))