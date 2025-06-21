# 金額を取得
money = int(input())

# 嬉しさ指数を計算し出力
hcnt_500 = money // 500
money = money - (hcnt_500 * 500)
hcnt_5 = (money // 5)
hcnt = (hcnt_500 * 1000) + (hcnt_5 * 5)
print(hcnt)