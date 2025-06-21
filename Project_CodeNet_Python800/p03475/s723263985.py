n=int(input())
C=[]
S=[]
F=[]
for i in range(n-1):
    c,s,f=map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)

ans=[0]*n
for i in range(n-1):
    t=0
    for j in range(i, n-1):
        if t<=S[j]:
            t=S[j]
        elif t%F[j]==0:
            pass
        else:
            t=(t//F[j]+1)*F[j]
        t+=C[j]
    ans[i]=t

for i in range(n):
    print(ans[i])  