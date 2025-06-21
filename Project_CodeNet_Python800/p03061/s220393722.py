from functools import reduce
from fractions import gcd

def main():
    n = int(input())
    a = sorted(int(i) for i in input().split())
    a0 = a[0]
    if a0 == 1:
        print(reduce(gcd, a[1:]))
        return
    c = []
    for i in range(2, int(a0**0.5) + 1):
        while a0 % i == 0:
            c.append(i)
            a0 //= i
    if a0 != 1:
        c.append(a0)
    d = [0] * len(c)
    for ai in a[1:]:
        for i, ci in enumerate(c):
            if ai % ci == 0:
                ai //= ci
            else:
                d[i] += 1
    e = []
    g = 1
    for k, v in zip(c, d):
        if v == 0:
            g *= k
        elif v == 1:
            e.append(k)
    f = [1] * (n - 1)
    for i, ai in enumerate(a[1:]):
        for ei in e:
            if ai % ei == 0:
                ai //= ei
            else:
                f[i] *= ei
    print(max(g * max(f), reduce(gcd, a[1:])))

if __name__ == '__main__':
    main()