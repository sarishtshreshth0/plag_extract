def jubge_winner():
    # 弱い順の数字をリスト化
    weak_strong_trump = [2,3,4,5,6,7,8,9,10,11,12,13,1]
    # ドロー
    A, B = map(int, input().split())
    # 大小判定
    A = weak_strong_trump.index(A)
    B = weak_strong_trump.index(B)
    # 結果
    if A > B:
        return 'Alice'
    elif A == B:
        return 'Draw'
    elif A < B:
        return 'Bob'

# 実行
result = jubge_winner()
print(result)