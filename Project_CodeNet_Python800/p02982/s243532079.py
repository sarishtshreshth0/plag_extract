r=input().split()
N=int(r[0])
D=int(r[1])
d=[[int(s) for s in input().split()] for i in range(N)]
ans=0
for i in range(N-1):
    for j in range(i+1,N):
        dis=0
        for k in range(D):
            dis+=(d[i][k]-d[j][k])**2
        ans_pre=dis**(1/2)
        if type(ans_pre)==int or ans_pre.is_integer()==True:
            ans+=1
print(ans)