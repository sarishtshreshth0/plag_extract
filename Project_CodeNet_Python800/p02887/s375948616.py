n=int(input())
s=input()
tmp=s[0]
ans=1
for i in range(1,n):
    if s[i]!=tmp:
        tmp=s[i]
        ans+=1
print(ans)