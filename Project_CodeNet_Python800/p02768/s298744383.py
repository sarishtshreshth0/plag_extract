p = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
n,a,b = map(int,input().split())
A = [1 for _ in range(2*10**5+1)]
for i in range(2,2*10**5+1):
    A[i] = (A[i-1]*i)%p
B = [1 for _ in range(2*10**5+1)]
B[2*10**5] = pow(A[2*10**5],p-2)
for i in range(2*10**5-1,1,-1):
    B[i] = (B[i+1]*(i+1))%p
cnt = pow(2,n)-1
cnt1 = 1
for i in range(a):
    cnt1 = (cnt1*(n-i))%p
cnt1 = (cnt1*B[a])%p
cnt2 = 1
for i in range(b):
    cnt2 = (cnt2*(n-i))%p
cnt2 = (cnt2*B[b])%p
cnt = (cnt-cnt1-cnt2)%p
print(cnt)