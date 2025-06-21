N, D = map(int, input().split())
coordinates = []

for _ in range(N):
    line = tuple(map(int, input().split()))
    coordinates.append(line)

count = 0
for i in range(N):
    for j in range(i+1, N):

        total = 0
        for y, z in zip(coordinates[i], coordinates[j]):
            total += abs(y - z) ** 2
    
        for k in range(1, total+1):
            if k * k == total:
                count += 1

print(count)