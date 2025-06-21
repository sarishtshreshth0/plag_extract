s=list(input())
n=len(s)

p=['1']
q=['0']

for x in range(1,n):
  if p[x-1]=='0':
    p.append('1')
  else:
    p.append('0')
    
  if q[x-1]=='0':
    q.append('1')
  else:
    q.append('0')
  
ans=0
ans1=0
for i in range(n):
  if s[i]!=p[i]:
    ans+=1
  if s[i]!=q[i]:
    ans1+=1
    
print(min(ans,ans1))