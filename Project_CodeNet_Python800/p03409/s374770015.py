N = int(input())
# N, K = [int(i) for i in input().split()]

red_points = []
for i in range(N):
    a, b = [int(i) for i in input().split()]
    red_points.append([a, b])
red_points_x_asc = sorted(red_points)
blue_points = []
for i in range(N):
    c, d = [int(i) for i in input().split()]
    blue_points.append([c, d])
blue_points_x_asc = sorted(blue_points)

paired_r = []
for b in blue_points_x_asc:
    b_x = b[0]
    b_y = b[1]
    r_cands = []
    for r in red_points:
        r_x = r[0]
        r_y = r[1]
        if r_x < b_x and r not in paired_r:
            r_cands.append(r)
    r_cands_y_desc = sorted(r_cands, key=lambda x: x[1], reverse=True)
    for r in r_cands_y_desc:
        r_x = r[0]
        r_y = r[1]
        if b_y > r_y:
            paired_r.append(r)
            break

print(len(paired_r))



