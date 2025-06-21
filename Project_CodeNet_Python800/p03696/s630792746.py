n=int(input())
s=input()
l=r=0
for c in s:
  if c=='(': l+=1
  else: r+=1
  if r>l: s='('+s; l+=1
print(s+')'*(l-r))