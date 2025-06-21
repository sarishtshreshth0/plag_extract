n=int(input())
s=input()
ans=1
mark=s[0]
for a in s:
    if a!=mark:
        mark=a
        ans+=1
print(ans)