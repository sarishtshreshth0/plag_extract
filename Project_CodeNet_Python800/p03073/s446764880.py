s=input()
leng=len(s)
a=0 #0101
b=0 #1010
for i in range(leng):
  if i%2==0:
    if s[i]=="1":
      a+=1
    if s[i]=="0":
      b+=1
  if i%2==1:
    if s[i]=="0":
      a+=1
    if s[i]=="1":
      b+=1
if a>=b:
  print(b)
else:
  print(a)