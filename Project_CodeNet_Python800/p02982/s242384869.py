n,d=[int(x) for x in input().rstrip().split()]

l=[]
for i in range(n):
  X=[int(x) for x in input().rstrip().split()]
  l.append(X)

ans=0
for i in range(n):
  ni=l[i]
  for j in range(i+1,n):
    nj=l[j]
    now=0
    for s in range(d):
      now+=(ni[s]-nj[s])**2
    now=now**0.5
    if now.is_integer():
        ans+=1
print(ans)