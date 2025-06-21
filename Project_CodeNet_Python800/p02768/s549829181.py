n, a, b = map(int, input().split())
def sum_product_mod(a, n, m):
    """aから一つずつ引いたのをn回掛ける"""
    res = a
    for i in range(1, n):
        res = res * (a - i) % m
    return res

def pow_mod(n, p, m):
    res = 1
    while p > 0:
        if p & 1:
            res = res * n % m
        p >>= 1
        n = n * n % m
    return res

MOD = 10 ** 9 + 7
all_comb = pow_mod(2, n, MOD) - 1
a_comb = sum_product_mod(n, a, MOD) * pow_mod(sum_product_mod(a, a, MOD), MOD-2, MOD)
b_comb = sum_product_mod(n, b, MOD) * pow_mod(sum_product_mod(b, b, MOD), MOD-2, MOD)
ans = (all_comb - a_comb - b_comb) % MOD
# print(all_comb, a_comb, b_comb)
print(ans)