N=int(input())
D=list(map(int, input().split()))
if D[0]!=0:
    print(0)
    exit()
if 0 in D[1:]:
    print(0)
    exit()
D=sorted(D)
p=998244353
edge=[0]*(N)

ans=1
for i in range(N):
    d=D[i]
    if i==0:
        if d==0:
            edge[0]+=1
            continue
        else:
            print(0)
            exit()
    if d==0:
        print(0)
        exit()
    if edge[d-1]==0:
        print(0)
        exit()
    else:
        edge[d]+=1
        ans*=edge[d-1]
        ans%=p

print(ans%p)
