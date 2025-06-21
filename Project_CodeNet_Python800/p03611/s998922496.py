def resolve():
    from collections import defaultdict
    N = int(input())
    A = [int(i) for i in input().split()]
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    maxA = 0
    d = dict(d)
    for key in d.keys():
        sumA = d.get(key)
        if key - 1 in d:
            sumA += d.get(key - 1)
        if key + 1 in d:
            sumA += d.get(key + 1)
        maxA = max(maxA, sumA)
    print(maxA)

resolve()
