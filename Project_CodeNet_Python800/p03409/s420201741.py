X_INDEX = 0
Y_INDEX = 1


def solve():
    number_of_balls = int(input())
    red_points = [list(map(int, input().split())) for _ in range(number_of_balls)]
    blue_points = [list(map(int, input().split())) for _ in range(number_of_balls)]

    from operator import itemgetter
    blue_points.sort(key=itemgetter(X_INDEX))  # 青玉をx座標の昇順でソート
    red_points.sort(key=itemgetter(Y_INDEX), reverse=True)  # 赤玉をy座標の降順でソート

    # 青玉：x座標の小さいものからペアを作っていく
    # 赤玉：青玉のx座標よりも小さいものの中で、y座標が最大のものをペアとする
    number_of_pairs = 0  # 仲良しペアの数
    used_red_points = [False for _ in range(number_of_balls)]  # 使用済み赤玉情報
    # used_blue_points = [False for _ in range(number_of_balls)]  # 使用済み青玉情報
    for blue_i, blue_point in enumerate(blue_points):
        for red_i, red_point in enumerate(red_points):
            if red_point[X_INDEX] < blue_point[X_INDEX] and \
                    red_point[Y_INDEX] < blue_point[Y_INDEX] and \
                    not used_red_points[red_i]:
                number_of_pairs += 1
                used_red_points[red_i] = True
                break

    print(number_of_pairs)


solve()