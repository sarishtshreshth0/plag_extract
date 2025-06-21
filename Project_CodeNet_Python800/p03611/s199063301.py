def tow_pointers(Q=1):

    # Q回分のクエリを処理
    for i in range(Q):

        # 合計値
        res = 0

        # 区間の左端で場合分け
        right = 0
        cnt = 0

        for left in range(n):
            while right < len(a) and a[left] + 2 >= a[right]:
                cnt += 1
                right += 1

            res = max(res, cnt)

            # leftをインクリメントする準備
            if right == left: right += 1
            else: cnt -= 1

        print(res)


n = int(input())
a = list(map(int, input().split()))
a.sort()
tow_pointers()
