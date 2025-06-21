import itertools
n=int(input())
sm=0
l=["3","5","7"]
for i in range(3,len(str(n))+1):
  b=list(itertools.product(l, repeat=i))
  for m in b:
    s="".join(m)
    if int(s)<=n and "7" in s and "3" in s and "5" in s:sm+=1
       
print(sm)