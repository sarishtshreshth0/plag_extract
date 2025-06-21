n=int(input())
w=["a"]*n
for i in range(n):
  w[i]=input()
c=0
for i in range(1,n):
  a=w.count(w[i])
  if a!=1:
    c+=1
    break
  if w[i-1][-1]!=w[i][0]:
    c+=1
    break
    
if c==0:
  print("Yes")
else:
  print("No")