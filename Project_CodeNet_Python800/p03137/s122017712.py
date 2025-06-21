N, M = map(int, input().split())
X = list(sorted(map(int, input().split())))

if N >= M:
    print(0)
else:
    D = []
    for i in range(len(X)-1):
        D.append(abs(X[i]-X[i+1]))
    D = list(sorted(D))
    print(sum(D[:M-N]))
