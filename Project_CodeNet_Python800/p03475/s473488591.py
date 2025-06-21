n=int(input())
c=[]
s=[]
f=[]

for i in range(n-1):
    C,S,F=map(int,input().split())
    c.append(C)
    s.append(S)
    f.append(F)
T=[-1]*n
T[-1]=0
for i in range(n-1):
    p=i
    t=0
    for j in range(n-i-1):
        if t<=s[p]:
            t=s[p]
            t+=c[p]
        else:
            m=(t+f[p]-1)//f[p]
            t=m*f[p]
            t+=c[p]
        p+=1
    T[i]=t
for i in range(n):
    print(T[i])
