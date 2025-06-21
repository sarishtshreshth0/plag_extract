N=int(input())
S=list(input())
check=""
ans=0
for i in range(N):
  if check!=S[i]:
    ans+=1
    check=S[i]
print(ans)
