n  = int(input())
red = [list(map(int,input().split())) for i in range(n)]
blue = [list(map(int,input().split())) for i in range(n)]

red.sort(reverse=True)
blue.sort()

ans = 0
for i in range(n):
    x = red[i][0]
    y = red[i][1]
    index = -1
    now_by = 201
    for j in range(len(blue)):
        if x < blue[j][0] and y < blue[j][1] and now_by > blue[j][1]:
            index = j
            now_by = blue[j][1]
    if index >= 0:
        ans += 1
        blue.pop(index)


print(ans)