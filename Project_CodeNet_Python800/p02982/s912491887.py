def dist(a, b, d):
    s = 0
    for i in range(d):
        s += (a[i] - b[i])**2
    
    return s

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

square_list = set([i*i for i in range(40*40*10+1)])

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if dist(X[i], X[j], D) in square_list:
            cnt += 1

print(cnt)