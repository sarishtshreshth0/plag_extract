N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]
blue.sort()
flg = [0]*N
for i in range(N):
    tmp_y = -1
    tmp_index = -1
    for k in range(N):
        if blue[i][0] > red[k][0] and flg[k] == 0:
            if tmp_y < red[k][1] and blue[i][1] > red[k][1]:
                tmp_y = red[k][1]
                tmp_index = k
    if tmp_index != -1:
        flg[tmp_index] = 1
print(flg.count(1))