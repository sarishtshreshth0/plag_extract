def comb(n, k, mod):

    m = 1
    for i in range(n, n - k, -1):
        m = m * i % mod

    n = 1
    for i in range(1, k + 1):
        n = n * i % mod

    return (m * pow(n, mod - 2, mod) % mod)


def main():

    mod = 1000000007
    n, a, b = map(int, input().split())

    ans = pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)
    ans = ans % mod
    print(ans)


if __name__ == '__main__':
    main()
