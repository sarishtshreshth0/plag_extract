S=input()
s1="01"*(len(S)//2+1)
ans1=0
ans2=0
for x in range(len(S)):
  if S[x]==s1[x]:
    ans2 +=1
  else:
    ans1 +=1
print(min(ans1,ans2))