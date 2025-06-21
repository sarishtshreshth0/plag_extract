N = int(input())


def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    mod = x % y
    if mod == 0:
        return y

    return gcd(y, mod)


def lcm(a, b):
    return a*b//gcd(a, b)


print(lcm(2, N))
