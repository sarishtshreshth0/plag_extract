s=input()
n=len(s)
d=[]
for i in range(n):
  d.append(int(s[i]))
s1=[0]
s2=[1]
for i in range(1,n):
  if s1[i-1]==0:
    s1.append(1)
  else:
    s1.append(0)
  if s2[i-1]==1:
    s2.append(0)
  else:
    s2.append(1)
a,b=0,0
for i in range(n):
  if d[i]!=s1[i]:
    a+=1
  if d[i]!=s2[i]:
    b+=1
print(min(a,b))