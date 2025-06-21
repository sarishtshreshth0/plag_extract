N=int(input())
D=list(map(int,input().split()))
MOD=998244353
if D[0]!=0:
    print(0)
    exit()
b=[0]*N
for d in D:
    b[d]+=1
if b[0]!=1:
    print(0)
    exit()

cnt=1
#print(b)
#print(b[1:])
for v1,v2 in zip(b,b[1:]):
    #print(v1)
    #print(v2)
    cnt *= v1**v2 % MOD
print(cnt%MOD)