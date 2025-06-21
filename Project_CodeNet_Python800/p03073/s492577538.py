S=list(map(int,input()))

ans1=0
for i in range(0,len(S),2):
  if S[i]==1:
    ans1+=1
for i in range(1,len(S),2):
  if S[i]==0:
    ans1+=1

ans2=0
for i in range(0,len(S),2):
  if S[i]==0:
    ans2+=1
for i in range(1,len(S),2):
  if S[i]==1:
    ans2+=1

print(min(ans1,ans2))
