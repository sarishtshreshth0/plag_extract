from itertools import product
n=int(input())
a=[]
for i in range(3,10):
  a+=(list(product('357',repeat=i)))
cnt=0
for i in a:
  if len(set(i))!=3:
    continue
  if int(''.join(list(i)))<=n:
    cnt+=1
  else:break
print(cnt)