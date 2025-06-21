N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]
# y座標で降順ソート
red.sort(reverse=True)
# x座標でソート
blue.sort(key=lambda x: x[1])

# print(blue)
# print(red)
blue_list = [0] * N
red_list = [0] * N


for b in range(N):
    for r in range(N):
        if blue_list[b] == 1 or red_list[r] == 1:
            continue
        if red[r][0] < blue[b][0] and red[r][1] < blue[b][1]:
            # print(b, r)
            blue_list[b] = 1
            red_list[r] = 1
            break

print(sum(blue_list))
