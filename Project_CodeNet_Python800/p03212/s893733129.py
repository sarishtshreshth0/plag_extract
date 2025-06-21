import itertools


n=int(input())
ans=0

for i in range(3,10):
  for lst in itertools.product(['3','5','7'],repeat=i):
    if '3' in lst and '5' in lst and '7' in lst:
      lst=''.join(lst)
      lst=int(lst)
      if n>=lst:
        ans+=1
        

print(ans)