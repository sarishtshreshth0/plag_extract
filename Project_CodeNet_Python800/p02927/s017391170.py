M, D = map(int, input().split())
ans = 0
for i in range(1, M+1):
    for j in range(1, D+1):
        if j % 10 < 2 or j // 10 < 2:
            continue
        else:
            j_str = str(j)
            mul = int(j_str[0]) * int(j_str[1])
            if mul == i:
                ans += 1
print(ans)