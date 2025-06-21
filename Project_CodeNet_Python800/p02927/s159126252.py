m, d = map(int, input().split())
cnt = 0
for i in range(1, m+1):
    for j in range(20, d+1):
        tenth = j // 10
        oneth = j % 10
        if oneth >= 2 and i == tenth * oneth:
            cnt +=1
        else:
            pass
print(cnt)
