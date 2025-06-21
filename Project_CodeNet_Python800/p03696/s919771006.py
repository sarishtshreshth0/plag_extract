n=int(input())
s=input()
x=s

for i in range(50):
  x=x.replace('()','')

l=x.count(')')
r=x.count('(')

for i in range(l):
  s='('+s

for i in range(r):
  s+=')'
  

print(s)