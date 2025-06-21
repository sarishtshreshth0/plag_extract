m,d=map(int,input().split())
c=0
for i in range(10,d):
  t=1
  flag=True
  for j in list(str(i+1)):
    if int(j)<2:
      flag=False
    t*=int(j)
  if not flag:
    continue
  if t<=m and t!=0:
    c+=1
print(c)