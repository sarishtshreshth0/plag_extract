N, D = map(int, input().split())
coordinates = []
c_append = coordinates.append
count = 0

for _ in range(N):
    X = list(map(int, input().split()))
    c_append(X)

for i in range(N-1):
    for j in range(i+1, N):
        distance = 0
        tmp1 = coordinates[i]
        tmp2 = coordinates[j]
        for k in range(D):
            distance += (tmp1[k] - tmp2[k]) ** 2
        distance = distance ** (1/2)
        if distance == int(distance):
            count += 1

print(count)
