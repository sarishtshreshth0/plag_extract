s=input()
i=0
c=0
for m in s:
  if i % 2 ==0:
    if int(m) ==1:
      c+=1
  else:
    if int(m)==0:
      c+=1
  i+=1
print(min(c,len(s)-c))