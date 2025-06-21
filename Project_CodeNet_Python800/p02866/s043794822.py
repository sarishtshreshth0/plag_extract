from collections import Counter
N=int(input())
D=list(map(int, input().split() ))
d=dict(Counter(D))
p=998244353
#print(d)
maxi=max(d)

ans=1
if D[0]!=0:
  print(0)
else:
  if d[0]!=1:
    print(0)
  else:
    for i in range(1,maxi+1):
      if i not in d:
        print(0)
        exit()
      else:
        s =  (d[i-1]**d[i])%p
        ans = (ans * s)%p
    print(ans)