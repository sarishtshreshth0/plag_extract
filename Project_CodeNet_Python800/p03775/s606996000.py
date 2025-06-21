def enum_div_pairs(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append((i, n // i))
    return res


def f(x, y):
    return max(map(lambda z: len(str(z)), [x, y]))


N = int(input())
divs = enum_div_pairs(N)
print(min(f(x, y) for x, y in divs))

