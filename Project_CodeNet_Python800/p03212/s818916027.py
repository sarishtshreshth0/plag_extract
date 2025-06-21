from collections import deque

n=int(input())

a=[3,5,7]

b=deque(a)

while b:
  v=b.popleft()
  
  x=v*10+3
  y=v*10+5
  z=v*10+7
  if x<=n:
    a.append(x)
    b.append(x)
    
  if y<=n:
    a.append(y)
    b.append(y)
    
  if z<=n:
    a.append(z)
    b.append(z)
ans=0    
for i in a:
  l=str(i)
  if '3' in l and '5' in l and '7' in l:
    ans+=1
    
print(ans)