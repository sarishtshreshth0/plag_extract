N=int(input())
D=list(map(int,input().split()))
M=998244353

P=max(D)
L=[0]*(P+1)
for d in D:
    L[d]+=1

if not(L[0]==1 and D[0]==0):
    print(0)
    exit()

K=1
for i in range(P):
    K*=pow(L[i],L[i+1],M)
    K%=M
print(K)