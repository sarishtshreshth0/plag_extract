n, a, b = map(int, input().split())
mod = int(1e9) + 7
temp = pow(2, n, mod) - 1
fa, fb = 1, 1
tempa, tempb = 1, 1
for i in range(1, a+1):
    fa *= i
    fa %= mod

    tempa *= (n - i + 1)
    tempa %= mod
for i in range(1, b+1):
    fb *= i
    fb %= mod
    tempb *= (n - i + 1)
    tempb %= mod

a_t = tempa * pow(fa, mod-2, mod) % mod
b_t = tempb * pow(fb, mod-2, mod) % mod
ans = (temp - a_t - b_t) % mod
print(ans)