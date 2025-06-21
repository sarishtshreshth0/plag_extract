def main():
    n, a, b = map(int, input().split())
    p = 10 ** 9 + 7
    r = pow(2, n, p) - 1
    if (n - a) < a:
        a = n - a
    if (n - b) < b:
        b = n - b
    fac_na = 1
    for i1 in range(n, n - a, -1):
        fac_na = (fac_na * i1) % p
    fac_nb = 1
    for i1 in range(n, n - b, -1):
        fac_nb = (fac_nb * i1) % p
    fac_a = 1
    for i1 in range(1, a+1):
        fac_a = (fac_a * i1) % p
    fac_b = 1
    for i1 in range(1, b+1):
        fac_b = (fac_b * i1) % p

    an = fac_na * pow(fac_a, p-2, p)
    bn = fac_nb * pow(fac_b, p-2, p)
    an = an % p
    bn = bn % p
    r -= an
    if r < 0:
        r += p
    r -= bn
    if r < 0:
        r += p
    if r < 0:
        r += p
    print(int(r))


if __name__ == '__main__':
    main()