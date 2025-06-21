n,d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]

l = len(X)
cnt = 0

for i in range(l):
    for j in range(i+1, l):
        distance = sum((X[i][d]-X[j][d])**2 for d in range(d))**0.5
        if distance == int(distance):
            cnt += 1
        else:
            continue
            
print(cnt)