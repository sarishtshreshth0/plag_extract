n=int(input())
s=input()

k=s[0]
ans=1
for i in range(1,len(s)):
    if k!=s[i]:
        k=s[i]
        ans+=1

print(ans)