n=int(input())
a=input()
c=[]
pre=''
for x in a:
  if x!=pre:
    c.append(x)
  pre=x
print(len(c))
