m, d = map(int, input().split())
cnt = 0
for i in range(4, m+1):
    for j in range(1, d+1):
        if j >= 22:
            x = j // 10
            y = j % 10
            if x >= 2 and y >= 2 and (x * y) == i:
                cnt += 1
print(cnt)