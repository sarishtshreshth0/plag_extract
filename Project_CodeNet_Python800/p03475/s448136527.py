n=int(input())
a=[list(map(int,input().split())) for _ in range(n-1)]
ans=[]
for i in range(n):
    now=0
    for j in range(i,n-1):
        c,s,f=a[j]
        if s==now:
            k=0
        elif s>now:
            k=s-now
        else:
            if now%f!=0:
                k=f-now%f
            else:
                k=0
        now+=c+k
    print(now)