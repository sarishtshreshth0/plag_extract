def comb_mod(n,r,m):
    ans = 1
    for i in range(1,r+1):
        ans *= (n-i+1) % m
        ans *= pow(i,m-2,m) % m
        ans = ans % m
    return ans
n,a,b = map(int,input().split())
m = 10**9 + 7
ans = pow(2,n,m) - comb_mod(n,a,m) - comb_mod(n,b,m) - 1
print(int(ans) % m)