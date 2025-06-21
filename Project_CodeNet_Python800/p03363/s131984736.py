def resolve():
    import math as m
    from collections import defaultdict
    N = int(input())
    A = [int(i) for i in input().split()]
    preSum = [0] * (N + 1)
    dd = defaultdict(int)
    dd[0] = 1
    for i in range(N):
        preSum[i + 1] = preSum[i] + A[i]
        dd[preSum[i] + A[i]] += 1
    sumA = 0
    for key in dd.keys():
        if dd[key] > 1:
            sumA += m.factorial(dd[key]) // (m.factorial(dd[key] - 2) * 2)
    print(sumA)


resolve()
