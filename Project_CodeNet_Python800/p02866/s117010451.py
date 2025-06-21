N=int(input())
D=list(map(int,input().split()))
mod=998244353

if D[0]!=0:
    print(0)
    exit()


B=[0]*N
for d in D:
    B[d]+=1
if B[0]!=1:
    print(0)
    exit()

ans=1
total=1
for i in range(1,N):
    if B[i]==0:
        if total!=N:
            print(0)
            exit()
        else:break
    total+=B[i]
    ans*=(B[i-1]**B[i])
    ans%=mod

print(ans)