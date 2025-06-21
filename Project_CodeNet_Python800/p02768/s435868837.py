n,a,b = map(int,input().split())

mod = pow(10,9)+7
ans = pow(2,n,mod)
ans -= 1
def choose(n,k):
    x,y = 1,1
    for i in range(1,k+1):
        x *= (n-i+1)
        x %= mod
        y *= i
        y %= mod
    
    x *= pow(y,mod-2,mod)
    x %= mod
    return x

ans -= choose(n,a)
ans -= choose(n,b)
ans %= mod
print(ans)