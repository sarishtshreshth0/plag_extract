n=int(input())
c=[];s=[];f=[]
for i in range(n-1):
    ci,si,fi=map(int,input().split())
    c.append(ci);s.append(si);f.append(fi)
for i in range(n-1):
    ans=s[i]+c[i]
    for j in range(i+1,n-1):
        tmp=ans
        if s[j]>=tmp:
            ans+=s[j]-tmp+c[j]
        else:
            ans+=f[j]-((tmp-s[j])%f[j] if (tmp-s[j])%f[j]!=0 else f[j])+c[j]
    print(ans)
print(0)