def choose(n, a):
    global mod
    x, y = 1, 1
    for i in range(a):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    return x * pow(y, mod - 2, mod) % mod

n,a,b = map(int,input().split())
mod = pow(10,9)+7
all = pow(2,n,mod)-1
print((all-choose(n,a)-choose(n,b))%mod)