def resolve():
    import math
    N, D = [int(i) for i in input().split()]
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            sumA = 0
            for k in range(D):
                sumA += (X[j][k] - X[i][k])**2
            if math.sqrt(sumA).is_integer():
                cnt += 1
    print(cnt)


resolve()
