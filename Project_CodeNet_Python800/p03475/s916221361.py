n = int(input())
csf=[]
for _ in range(n-1):
    c,s,f=map(int,input().split())
    csf.append((c,s,f))
ans=[0]*n
for i,(c,s,f) in enumerate(csf):
    for j in range(0,i+1):
        if ans[j]<=s:
            ans[j]=s+c
        else:
            ans[j]=(ans[j]+f-1)//f*f+c
for x in ans:
    print(x)