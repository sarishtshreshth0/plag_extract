p = 10**9+7
def power_func(a,n):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %p
        if bi[i]=="1":
          res=(res*a) %p
    return res
g1,g2,inverse = [1, 1],[1, 1],[0, 1]
for i in range(2,2*(10**5)+1):
    g1.append((g1[-1]*i)%p)
    inverse.append((-inverse[p%i]*(p//i))%p)
    g2.append((g2[-1]*inverse[-1])%p)
n,a,b= map(int,input().split())
comnk=1
temp1=-1
for i in range(b):
    comnk=(((comnk*(n-i))%p)*inverse[i+1])%p
    if i==a-1:temp1=(power_func(2,n)-1+p-comnk)%p
print((temp1 + p - comnk) % p)