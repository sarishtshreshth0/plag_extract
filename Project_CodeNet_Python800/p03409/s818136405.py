N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]
red.sort(reverse=True)
blue.sort(key=lambda x:x[1])
blue_check = [0]*N
for i in range(N):
    for k in range(N):
        if blue_check[k] == 1:
            continue
        if red[i][0] < blue[k][0] and red[i][1] < blue[k][1]:
            blue_check[k] = 1
            break
print(sum(blue_check))
