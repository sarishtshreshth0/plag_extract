from collections import deque
n=int(input())
s=input()
ans=deque(s)
cnt=0
for i in range(n):
  if (cnt==0)and(s[i]==')'):
    ans.appendleft('(')
  elif (cnt!=0)and(s[i]==')'):
    cnt-=1
    pass
  elif s[i]=='(':
    cnt+=1
if cnt>0:
  ans.append(')'*cnt)
print(''.join(ans))