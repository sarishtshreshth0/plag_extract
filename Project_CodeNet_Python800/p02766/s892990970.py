N, K = map(int,input().split())

t = 0
for i in range(N):
    N = N//K
    t += 1
    if N == 0:
        print(t)
        exit()