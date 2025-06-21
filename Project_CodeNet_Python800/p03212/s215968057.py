def f(L,X=[]):
    if L==1:
        return ["3","5","7"]
    else:
        X=f(L-1)
        Y=[]
        for x in X:
            Y+=[x+"3",x+"5",x+"7"]
        return Y
    
N=int(input())
G=[]
for k in range(1,10):
    V=f(k)
    
    for v in V:
        if ("3" in v) and ("5" in v) and ("7" in v):
            G.append(int(v))

T=0
for x in G:
    if x<=N:
        T+=1

print(T)
