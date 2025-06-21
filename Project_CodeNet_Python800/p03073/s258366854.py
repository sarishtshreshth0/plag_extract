s=input()
b=c=0
for i in s:
  c+=(int(i)==b)
  b^=1
print(min(c,len(s)-c))