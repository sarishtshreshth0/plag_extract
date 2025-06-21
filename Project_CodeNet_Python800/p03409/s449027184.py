def c_2d_plane_2n_points():
    N = int(input())
    R = [tuple([int(i) for i in input().split()]) for j in range(N)]
    B = [tuple([int(i) for i in input().split()]) for j in range(N)]

    red = sorted(R, key=lambda x: x[1], reverse=True)  # 赤い点の座標 (y 座標で降順ソート)
    blue = sorted(B)  # 青い点の座標 (x 座標で昇順ソート)
    ans = 0
    for x_b, y_b in blue:
        for x_r, y_r in red:
            # 注目している青い点より xy 平面で左下にある赤い点のうち、
            # 最も右上にある点とマッチさせるのが最適
            if x_b > x_r and y_b > y_r:
                ans += 1
                red.remove((x_r, y_r))  # もう選べないので削除
                break  # この青い点ももう選べないので終了
    return ans

print(c_2d_plane_2n_points())