def cmb(n, r, p):
    r = min(r, n - r)

    # n*(n-1)*...*(n-r+1)
    # 組み合わせの分子
    upper = 1
    for i in range(n, n - r, -1):
        upper = (upper * i) % p

    # 1*2*...*r
    # 組み合わせの分母
    lower = 1
    for i in range(1, r + 1):
        lower = (lower * i) % p
    # 剰余の計算において、+-*は良いが、/は普通にやると成り立たない
    # 割るのではなく、「逆元」を掛けるとする
    # フェルマーの小定理より、pが素数なら1/lowerの逆元はlower**(p-2)
    # powの第3引数を使うことで繰り返し二乗法になる
    return (upper * pow(lower, p - 2, p)) % p


mod = pow(10, 9) + 7
n, a, b = map(int, input().split())
# 全ての選び方-何も選ばない時-a本の時-b本の時
ans = (pow(2, n, mod) - 1 - cmb(n, a, mod) - cmb(n, b, mod)) % mod
print(ans)
