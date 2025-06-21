m, d = map(int, input().split())
ans = 0
for i in range(4, m + 1):
    for j in range(22, d + 1):
        arr = str(j)
        if int(arr[0]) >= 2 and int(arr[1]) >= 2 and i == int(arr[0]) * int(arr[1]):
            ans += 1
print(ans)
