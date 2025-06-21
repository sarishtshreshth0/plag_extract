def combinations_mod(n, r, mod=1000000007):
    """Returns nCr in mod."""
    r = min(r, n - r)
    combs = 1
    for i, j in zip(range(n - r + 1, n + 1), range(1, r + 1)):
        combs *= (i % mod) * pow(j, mod - 2, mod)
        combs %= mod
    return combs


def main():
    n, a, b = [int(x) for x in input().split()]
    mod = 1000000007
    total = pow(2, n, mod) - 1
    ans = total - combinations_mod(n, a) - combinations_mod(n, b)
    ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
