input()
c=[0]*100002
for i in map(int,input().split()):
  for j in (0,1,2): c[i+j]+=1
print(max(c))