n,a,b=list(map(int, input().split()))
C=10**9+7

def perm(a,b):
    tmp=1
    for i in range(b):
        tmp*=a-i
        tmp=tmp%C
    return tmp

cta=perm(n,a)*pow(perm(a,a),C-2,C)
ctb=perm(n,b)*pow(perm(b,b),C-2,C)

ans=pow(2,n,C)-1-cta-ctb
print(ans%C)