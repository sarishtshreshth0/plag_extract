p=998244353
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
N = int(input())
D = list(map(int,input().split()))
D.insert(0,0)
C = {i:0 for i in range(N)}
for i in range(1,N+1):
    C[D[i]] += 1
if C[0]!=1 or D[1]!=0:
    cnt = 0
else:
    ind = 0
    for i in range(N):
        if C[i]==0:
            ind = i
            break
    flag = 0
    if ind>0:
        for i in range(ind+1,N):
            if C[i]>0:
                flag = 1
                break
    if flag==1:
        cnt = 0
    else:
        C = sorted(list(C.items()),key=lambda x:x[0])
        cnt = 1
        for i in range(1,N):
            if C[i][1]==0:break
            c0 = C[i-1][1]
            c1 = C[i][1]
            cnt = (cnt*(pow(c0,c1)))%p
print(cnt)