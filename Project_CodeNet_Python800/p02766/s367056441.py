n,k = map(int,input().split())
if(n//k==0):
  a =0
else:
  a = 1
for i in range(100000000000):
  n =  n//k
  a +=1
  if(n<k):
    break
print(a)