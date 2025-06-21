n=int(input())
L=[]
for _ in range(n-1):
    L.append(tuple(map(int,input().split())))
ans=[]
for i in range(n-1):
    c,t,f=L[i]
    t += c
    for j in range(i+1,n-1):
        cn,sn,fn=L[j]
        if t>sn:
            t=-int(-t//fn)*fn
        else:
            t=sn
        t += cn
    ans.append(t)
ans.append(0)
for i in ans:
    print(i)