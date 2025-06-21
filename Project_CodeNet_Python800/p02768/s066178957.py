def main():
    from functools import reduce
    def a_comb_mod(n, r):
        mod = 1000000007
        r = min(n-r,r)
        if r == 0: return 1
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1), 1)
        denom = reduce(lambda x, y: x * y % mod, range(1,r + 1), 1)
        denom_inv = pow(denom, mod - 2, mod)
        return numer * denom_inv % mod

    n, a, b = list(map(int, input().split()))
    mod = 1000000007
    print((pow(2, n, mod) - 1 - a_comb_mod(n, a) - a_comb_mod(n, b)) % mod)

if __name__ == '__main__':
    main()
