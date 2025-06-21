n=int(input())
s=input()
cnt=0
ans=str()
for i in range(n):
    if s[i]=="(":
        cnt+=1
        ans+="("
    elif s[i]==")":
        if cnt>0:
            cnt-=1
            ans+=")"
        else:
            ans=ans[::-1]
            ans+="("
            ans=ans[::-1]
            ans+=")"
            cnt=0

if cnt>0:
    while cnt>0:
        ans+=")"
        cnt-=1

print(ans)