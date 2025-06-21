# ΣnCiが高速に計算できればいいがNがでかい -> なんかΣncrでググったら高速化できるらしい?
# なんかi=0 -> i=nで2^nになるらしい。これは繰り返し二乗法でいけそう

# 最終的にΣnCi(i=1, i<=n) - nCa - nCaができればいい

# なぜか手持ちのライブラリがことごとくダメ

n, a, b = map(int, input().split())
mod = 10**9 + 7


def rep(i, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        tmp = rep(i, n // 2) % mod
        return tmp * tmp % mod
    else:
        return i * rep(i, n - 1) % mod


# なぜかうまくいかない
# def ncr(n, r):
#     res = 1
#     for i in range(1, r + 1):
#         res = res * (n - i + 1) // i
#         res %= mod
#     for i in range(2, r + 1):
#         res *= rep(i, mod - 2)
#         res %= mod
#     return res

# なぜかうまくいかない
# def cmb(n, r, mod):
#     if (r < 0 or r > n):
#         return 0
#     g1 = [1, 1]  # 元テーブル
#     g2 = [1, 1]  #逆元テーブル
#     inverse = [0, 1]  #逆元テーブル計算用テーブル
#     N = 10**6  # なんでだろうね
#     for i in range(2, N + 1):
#         g1.append((g1[-1] * i) % mod)
#         inverse.append((-inverse[mod % i] * (mod // i)) % mod)
#         g2.append((g2[-1] * inverse[-1]) % mod)
#     return g1[n] * g2[r] * g2[n - r] % mod


# なぜかうまくいく
def nCrMod(n, r, p):
    ret = 1
    # 分子
    for i in range(n - r + 1, n + 1):
        ret *= i
        ret %= p
    # 分母
    for i in range(2, r + 1):
        # ret //= i なんかこれがおかしい（なんでだろうね）
        ret *= rep(i, p - 2)  # なぜかここでやらないと駄目だった
        ret %= p
    # ret = repMod(ret, p - 2, p) # なぜかここでやると駄目だった
    return ret % p


ans = (rep(2, n) - 1 - nCrMod(n, a, mod) - nCrMod(n, b, mod)) % mod  # なぜかうまくいく
# ans = (rep(2, n) - 1 - ncr(n, a) - ncr(n, b)) % mod なぜかうまくいかない
# ans = (rep(2, n) - 1 - cmb(n, a, mod) - cmb(n, b, mod)) % mod なぜかうまくいかない
while ans < 0:
    ans += mod
print(ans)
