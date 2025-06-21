n=int(input())
a=[list(map(int,input().split())) for _ in range(n-1)]
for i in range(n):
    t=0
    for c,s,f in a[i:]:
        k=max(0,(t-s+f-1)//f)
        t=s+f*k+c
    print(t)