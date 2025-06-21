n = int(input())
red = []
blue = []
for _ in range(n):
    red.append(list(map(int, input().split())))
for _ in range(n):
    blue.append(list(map(int, input().split())))

# 赤はy座標が大きい順に取っていくので、yで降順
red.sort(key=lambda x: x[1], reverse=True)
# 青はx座標が小さい順に探していくので、xで昇順
blue.sort()

pair_count = 0
for i in range(n):
    for j in range(len(red)):
        if red[j][0] < blue[i][0] and red[j][1] < blue[i][1]:
            pair_count += 1
            red.pop(j)
            break

print(pair_count)