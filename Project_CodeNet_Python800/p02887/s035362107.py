n=int(input())
s=input()

ans=''
for i in range(n-1):
  if s[i]==s[i+1]:
    pass
  else:
    ans+=s[i]
    
ans+=s[-1]

print(len(ans))