N, K = list(map(int, input().rstrip().split()))
r = 0
while 0 < N:
    r += 1
    N = int(N / K)

print(r)

