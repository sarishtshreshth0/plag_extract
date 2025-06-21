a,b,c,d=map(int,input().split())
lisa=[]
for i in range(a,b):
  lisa.append(i)
lisb=[]
for j in range(c,d):
  lisb.append(j)
count=0
for k in range(0,len(lisa)):
  if lisa[k] in lisb:
    count+=1
print(count)