n, d = map(int, input().split())
x = []
sum_ = 0
count = 0

for ni in range(n):
    e = list(map(int, input().split()))
    x.append(e)

for i in range(n):
    for j in range(i+1,n):
        for k in range(d):
            sum_ += (x[i][k] - x[j][k])**2
        if sum_**0.5 % 1 == 0:
            count += 1
        sum_ = 0

print(count)