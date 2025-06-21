from fractions  import gcd


n=int(input())
a=list(map(int,input().split()))
inf = 0
num_min =2**(n-1).bit_length()
dat=[inf]*(2*num_min-1)

#初期化
for i in range(n):
    dat[i+num_min-1]=a[i]
for i in range(num_min-2,-1,-1):
    dat[i]=gcd(dat[2*i+1],dat[2*i+2])

#親のノード(n-1)//2
#子のノード2n+1,2n+2

def segfunc(x,y):
    return gcd(x,y)

def update(i,x):
    i+=n-1
    dat[i]=x
    while i>0:
        i=(i-1)//2
        dat[i]=segfunc(dat[2*i+1],dat[2*i+2])
def query(a,b): #半開区間、[a,b)の最小値
    if b<=a:
        return inf
    res=inf
    a += num_min-1
    b += num_min-2
    while b-a>1:
        if a&1==0:
            res = segfunc(res,dat[a])
        if b&1==1:
            res = segfunc(res,dat[b])
            b-=1
        a=a//2
        b=(b-1)//2
    if a==b:
        res = segfunc(res,dat[a])
    else:
        res=segfunc(segfunc(res,dat[a]),dat[b])
    return res

ans=0
for i in range(n):
    left=query(0,i)
    right=query(i+1,n)
    ans=max(ans,gcd(left,right))
print(ans)