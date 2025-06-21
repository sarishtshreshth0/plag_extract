s=input()
t=input()
S=len(s)
T=len(t)
ans=[[0 for e in range(S+1)] for f in range(T+1)]
chk=[]
for a in range(1,T+1):
 for b in range(1,S+1):
  if t[a-1]==s[b-1]:
   ans[a][b]=ans[a-1][b-1]+1
  else:
   if ans[a-1][b]>ans[a][b-1]:
    ans[a][b]=ans[a-1][b]
   else:
    ans[a][b]=ans[a][b-1]
x,y=T,S
while x>0 and y>0:
 if ans[x][y]==ans[x-1][y]:
  x-=1
 elif ans[x][y]==ans[x][y-1]:
  y-=1
 else:
  x-=1
  y-=1
  chk.append(s[y])
chk.reverse()
print("".join(chk))    