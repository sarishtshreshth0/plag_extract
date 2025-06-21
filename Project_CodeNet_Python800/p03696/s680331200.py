n=int(input())
s=input()
L=0
R=0
for i in s:
  if i==')':
    if R:R-=1
    else:L+=1
  else:
    R+=1
print('('*L+s+')'*R)