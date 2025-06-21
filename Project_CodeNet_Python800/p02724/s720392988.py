def happiness_from_golden_coins():
    # 入力
    X = int(input())
    # 初期化
    count_500yen = 0
    count_5yen = 0
    # 両替処理
    # 500円の個数
    while True:
        if X >= 500:
            count_500yen += 1
            X -= 500
        else:
            break
    # 5円の個数
    while True:
        if X >= 5:
            count_5yen += 1
            X -= 5
        else:
            break
    # 嬉しさ集計
    happiness = (1000 * count_500yen) + (5 * count_5yen)
    return happiness

result = happiness_from_golden_coins()
print(result)