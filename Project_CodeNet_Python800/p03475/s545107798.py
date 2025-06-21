n=int(input())
c=[]
s=[]
f=[]
for i in range(n-1):
    cc,ss,ff=map(int,input().split())
    c.append(cc)
    s.append(ss)
    f.append(ff)

for i in range(n-1):
    x=s[i]+c[i]
    for j in range(i+1,n-1):
        if x<=s[j]:
            x=s[j]+c[j]
        else:
            if (x-s[j])%f[j]==0:
                x+=c[j]
            else:
                t=int((x-s[j])/f[j])
                x=s[j]+f[j]*(t+1)+c[j]
    print(x)
print(0)