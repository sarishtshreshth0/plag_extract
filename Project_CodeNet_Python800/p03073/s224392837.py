s=input()
b=l=r=0
for i in s:
  l+=(int(i)==b)
  r+=(int(i)!=b)
  b^=1
print(min(l,r))