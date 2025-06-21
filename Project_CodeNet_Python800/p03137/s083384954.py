N, M = map(int, input().split())
X = list(input().split())
MAP = list(sorted([int(X[i]) for i in range(M)]))

if M <= N:
    print(0)
else:
    MAP_diff = list(sorted([MAP[i+1] - MAP[i] for i in range(M-1)]))
    print(sum(MAP_diff[:M-N]))