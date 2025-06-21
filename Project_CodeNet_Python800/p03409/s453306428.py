N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]

# 青をx座標で昇順ソート
blue.sort(key=lambda x: x[1])

# 赤をy座標で降順ソート
red.sort(key=lambda x: x[0], reverse=True)

red_list = [0] * N

for b in range(N):
    for r in range(N):
        if red_list[r] == 1:
            continue
        if red[r][0] < blue[b][0] and red[r][1] < blue[b][1]:
            red_list[r] = 1
            break

print(sum(red_list))
