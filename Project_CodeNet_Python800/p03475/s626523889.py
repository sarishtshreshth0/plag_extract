n = int(input())

csf = [list(map(int, input().split())) for _ in range(n-1)]

# start ~ 最終駅行くまでにかかる時間
#   timeで合算の時間を扱う
def reach(start, time):
    if start == n-1:
        return time

    # 電車が開通していない場合は開通まで待つ
    if time <= csf[start][1]:
        time = csf[start][1]
    else:
        while time % csf[start][2] != 0:
            time += 1
    return reach(start+1, time + csf[start][0])

for i in range(n-1):
    print(reach(i, 0))
print(reach(n-1, 0))