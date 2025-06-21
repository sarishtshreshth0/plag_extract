N = int(input())
# 問題文では駅は1-indexだが以下では0-indexにして考えている
CSF = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N):
    ans = 0
    for j in range(i, N - 1):
        # i,i+1,...,N-1番の駅からの電車について考える
        c, s, f = CSF[j][0], CSF[j][1], CSF[j][2]

        # ans = 今いる駅に着いた時刻

        # 以下、まず待ち時間に着いて考える

        # 開通前に着いてしまったら開通まで待つしかない
        # 発射時刻はs
        if ans < s:
            ans = s
        else:
            # 待ち時間無しで次に乗れる場合
            if ans % f == 0:
                ans += 0
            # 待ち時間が発生する場合
            # ex. F=5でt=7に到着する場合、待ち時間は5-7%5=3
            else:
                ans += f - ans % f

        # 次の駅までc秒かかる
        ans += c
    # i=0,1,2,...,n-1の全てについて、i駅からかかった時間
    print(ans)
