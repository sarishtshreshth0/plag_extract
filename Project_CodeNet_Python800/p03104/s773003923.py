A, B = map(int, input().split())


def f(first, last):
    diff = last - first
    m = diff % 4
    res = 0
    # print(first, last, last - m, last + 1)
    if first % 2 == 0:
        for i in reversed(range(last - m, last + 1)):
            res ^= i
        return res
    else:
        for i in reversed(range(last - m + 1, last + 1)):
            res ^= i
        res ^= first
        return res


print(f(A, B))

