N = int(input())

R = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

R = sorted(R, key=lambda x: -x[1])  # 赤い点はy座標が大きい順にする
B = sorted(B, key=lambda x: x[0])  # 青い点はx座標が小さい順にする

for a, b in B:  # 青い点, x座標が小さい順になっている
    for c, d in R:  # 赤い点, y座標が大きい順になっている
        if a > c and b > d:  # 青い点のx座標より赤い点のx座標が小さく, 青い点のy座標より赤い点のy座標が小さければペアにする
            R.remove([c, d])
            break

print(N - len(R))
