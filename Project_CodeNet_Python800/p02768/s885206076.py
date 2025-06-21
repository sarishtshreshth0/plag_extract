# N = int(input())
def cmb(n, r, mod):
    x = 1
    for i in range(r):
        x = x * (n-i) % mod
    return (x * g2[r]) % mod


mod = 10**9+7 #出力の制限
N = 2*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル


for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

def pow_(x, n):
    if n == 0:
        return 1

    k = 1
    while n > 1:
        if n % 2 != 0:
            k = (k * x) % MOD
        x = (x * x) % MOD
        n //= 2

    return (k * x) % MOD

n, a, b = [int(i) for i in input().split()]
MOD = 10 ** 9 + 7
n_num = pow_(2, n) - 1
a_num = cmb(n, a, MOD)
b_num = cmb(n, b, MOD)
print((n_num - a_num - b_num) % MOD)
