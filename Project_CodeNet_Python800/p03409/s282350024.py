n = int(input())
red_point_list = [[int(j) for j in input().split()] for i in range(n)]
blue_point_list = [[int(j) for j in input().split()] for i in range(n)]

count = 0
for c, d in sorted(blue_point_list, key=lambda x: x[0]):
    tmp_index = 0
    tmp_y = -1
    for i, p in enumerate(red_point_list):
        if c > p[0] and d > p[1]:
            if p[1] >= tmp_y:
                tmp_index = i
                tmp_y = p[1]

    if tmp_y > -1:
        count += 1
        red_point_list.pop(tmp_index)

print(count)