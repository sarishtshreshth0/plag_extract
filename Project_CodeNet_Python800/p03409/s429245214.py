"abc091c - 2D Plane 2N Points"
N = int(input())
reds = [list(map(int, input().split())) for _ in range(N)]
blues = [list(map(int, input().split())) for _ in range(N)]

# 赤い点をy座標による降順ソートする
reds.sort(key=lambda x: -x[1])
# 青い点をx座標による昇順ソートする
blues.sort(key=lambda x: x[0])
# 一番左側の青い点からマッチング相手を探していく
for c, d in blues:
    for a, b in reds:
        if a <= c and b <= d:
            reds.remove([a, b])
            break
print(N-len(reds))
