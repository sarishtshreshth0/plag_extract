m,d = map(int,input().split())
k = 0
for i in range(1,m+1):
    for j in range(1,d+1):
        x = j // 10
        if x < 2:
            continue
        y = j % 10
        if y < 2:
            continue
        if x * y == i:
            k += 1

print(k)