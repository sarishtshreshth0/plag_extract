n=int(input())
s=input()
ans=s
while len(s)>0:
  s=ans
  i=0
  while i<len(s):
    if s[i:i+2]=='()':
      s=(s[:i]+s[i+2:] if i!=0 else s[i+2:])
      i=-1
    i+=1
  l=s.count('(')
  r=s.count(')')
  if l>r :
    ans=ans+')'*(l-r)
  elif r>l:
    ans='('*(r-l)+ans
  elif len(s)>0:
    ans='('+ans
print(ans)