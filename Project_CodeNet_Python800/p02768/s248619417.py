def mod_pow(a, n, mod):
    """
    二分累乗法による a^n (mod m)の実装
    :param a: 累乗の底
    :param n: 累乗の指数
    :param mod: 法
    :return: a^n (mod m)
    """

    result = 1
    a_n = a
    while n > 0:
        if n & 1:
            result = result * a_n % mod
        a_n = a_n * a_n % mod
        n >>= 1
    return result


def mod_inverse(a, mod):
    """
    フェルマーの小定理による a^-1 ≡ 1 (mod m)の実装
    aの逆元を計算する
    a^-1 ≡ 1 (mod m)
    a * a^-2 ≡ 1 (mod m)
    a^-2 ≡ a^-1 (mod m)
    :param a: 逆元を計算したい数
    :param mod: 法
    :return: a^-1 ≡ 1 (mod m)
    """

    return mod_pow(a=a, n=mod - 2, mod=mod)


def mod_combination(n, k, mod):
    fact_n = 1
    fact_k = 1
    for i in range(k):
        fact_n *= (n - i)
        fact_n %= mod
        fact_k *= (i + 1)
        fact_k %= mod

    fact_n *= mod_inverse(fact_k, mod)
    return fact_n % mod


N, A, B = map(int, input().split(' '))
MOD = 10 ** 9 + 7

print((mod_pow(2, N, MOD) - 1 - mod_combination(N, A, MOD) - mod_combination(N, B, MOD)) % MOD)
