n=int(input())
s=list(input())
ans=0
i=0
while i+1<n:
  j=0
  while s[i+j]==s[i+j+1]:
    if i+j+1<=n-2:
      j+=1
    else:
      j+=1
      break
  i+=j+1
  ans+=j
  
print(n-ans)