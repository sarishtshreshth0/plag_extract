n, a, b = map(int, input().split())
mod = 10**9 + 7

modinv_table_a = [-1] * (a+1)
modinv_table_a[1] = 1
for i in range(2, a+1):
    modinv_table_a[i] = (-modinv_table_a[mod % i] * (mod // i)) % mod

modinv_table_b = [-1] * (b+1)
modinv_table_b[1] = 1
for i in range(2, b+1):
    modinv_table_b[i] = (-modinv_table_b[mod % i] * (mod // i)) % mod

def binomial_coefficients_a(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table_a[i + 1]
        ans %= mod
    return ans

def binomial_coefficients_b(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table_b[i + 1]
        ans %= mod
    return ans

res = (pow(2,n,mod)-binomial_coefficients_a(n,a)-binomial_coefficients_b(n,b)-1)%mod
print(res if res >= 0 else res+mod)