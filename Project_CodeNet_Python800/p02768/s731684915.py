def comb_mod(n, r, mod):
    up = 1
    down = 1
    for i in range(r):
        up *= n - i
        up %= mod
        down *= i + 1
        down %= mod
    return ((up * pow(down, mod - 2, mod)) % mod)


def main():
    MOD = 10**9 + 7
    n, a, b = [int(x) for x in input().split()]

    result = pow(2, n, MOD) - 1
    a_cmb = comb_mod(n, a, MOD)
    b_cmb = comb_mod(n, b, MOD)

    result = (result - a_cmb) % MOD
    result = (result - b_cmb) % MOD

    print(result)


if __name__ == '__main__':
    main()
