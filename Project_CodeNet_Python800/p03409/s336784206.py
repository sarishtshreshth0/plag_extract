n=int(input())
ab=[[int(i) for i in input().split()] for _ in range(n)]
cd=[[int(i) for i in input().split()] for _ in range(n)]
inab=[sum(map(lambda x:x[0]>a and x[1]>b,cd)) for a,b in ab]
incd=[sum(map(lambda x:x[0]<c and x[1]<d,ab)) for c,d in cd]
ans=0
while 1:
  f=1
  mab=1000
  for i in range(n):
    if inab[i] > 0 and mab > inab[i]:
      f=0
      mab=inab[i]
  if f:
    break
  mcd=1000
  tmp=(-1,-1)
  ans+=1
  for i in range(n):
    if mab==inab[i]:
      a,b=ab[i]
      for j in range(n):
        if incd[j]==0:continue
        c,d=cd[j]
        if a<c and b<d and mcd>incd[j]:
          mcd=incd[j]
          tmp=(i,j)
  ta,tb=ab[tmp[0]]
  tc,td=cd[tmp[1]]
  inab[tmp[0]]=0
  incd[tmp[1]]=0
  for i in range(n):
    a,b=ab[i]
    c,d=cd[i]    
    if inab[i]:
      if a<tc and b<td:
        inab[i]-=1
    if incd[i]:
      if c>ta and d>tb:
        incd[i]-=1  
print(ans)
