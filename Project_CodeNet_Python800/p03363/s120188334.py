N=int(input())
A=list(map(int,input().split()))

D={0:1}
S=0
for i in range(N):
    S+=A[i]
    if S in D:
        D[S]+=1
    else:
        D[S]=1

K=0
for a in D:
    K+=(D[a]*(D[a]-1))//2

print(K)
