N,D=map(int,input().split())
z=[]
for i in range(N):
    x=list(map(int,input().split()))
    z.append(x)
def judge_dis(K,L):
    d=0
    for k,l in zip(K,L):
        d+=(k-l)**2
    import math
    d=math.sqrt(d)
    return d.is_integer()
ans=0
for x in range(N-1):
    for i in range(x+1,N):
        if judge_dis(z[x],z[i]):
            ans+=1
print(ans)
