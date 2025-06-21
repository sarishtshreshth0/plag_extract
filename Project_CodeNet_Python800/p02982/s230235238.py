squares = set({})
for i in range(1,130):
    squares.add(i**2)

N,D=map(int,input().split())
n = 0
X = []
for _ in range(N):
    X.append(list(map(int,input().split())))

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        sum = 0
        for k in range(D):
            sum += (X[i][k]-X[j][k])**2
        if sum in squares:
            ans += 1

print(ans)