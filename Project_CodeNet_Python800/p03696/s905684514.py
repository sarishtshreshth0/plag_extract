n=int(input())
s=input()

p=0
q=0
for i in s:
  if i=='(':
    p+=1
  else:
    if p>=1:
      p-=1
    else:
      q+=1
      p=0

ans='('*q+s+')'*p
print(ans)