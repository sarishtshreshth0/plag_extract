from functools import reduce

def main():
    n, a, b = map(int, input().split())
    p = 10 ** 9 + 7

    ans = pow(2, n, p) - 1

    print((ans - comb(n,a,p) - comb(n,b,p)) % p)

def comb(n, r, p):
    r = min(r, n-r)
    if r == 0:
        return 1
    
    num = reduce(lambda x, y: (x * y) % p, range(n, n - r, -1))
    den = reduce(lambda x, y: (x * y) % p, range(1, r + 1))

    return (num * pow(den, p - 2, p)) % p

if __name__ == '__main__':
    main()