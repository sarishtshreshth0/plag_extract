def resolve():
    N, D = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    import itertools
    for i, j in itertools.combinations(list(range(N)), 2):
        dist = 0
        for d in range(D):
            dist += (X[i][d] - X[j][d])**2
        dist = dist**(0.5)
        if dist == int(dist):
            cnt += 1
    print(cnt)
    
if '__main__' == __name__:
    resolve()