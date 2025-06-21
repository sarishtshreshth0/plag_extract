n=input()
k=int(n)
gou=0
for i in range(len(n)):
  gou+=int(n[i])
if k%gou==0:
  print("Yes")
else:
  print("No")