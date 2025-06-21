n=int(input())
csf=[list(map(int,input().split())) for _ in range(n-1)]
#n=100000
#csf=[[1,0,1] for _ in range(n-1)]
for i in range(n-1):
    t=0
    for j in range(i,n-1):
        t=max(csf[j][1],t+(-t)%csf[j][2])+csf[j][0]
    print(t)
print(0)