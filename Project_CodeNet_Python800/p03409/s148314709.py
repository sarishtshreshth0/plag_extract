N = int(input())
red = sorted([list(map(int,input().split())) for i in range(N)], key=lambda x: x[0])[::-1]
blue = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(N):
    min_ = 10 ** 9 + 7
    ind = -1
    for j in range(N):
        if red[i][0] <= blue[j][0] and red[i][1] <= blue[j][1] and blue[j][1] < min_:
            ind = j
            min_ = blue[j][1]
    if ind != -1:
        blue[ind][0] = -1
        ans += 1
print(ans)