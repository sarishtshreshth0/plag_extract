# A - One Card Poker

# Alice と Bob は 2人で1枚のポーカーをやっている
# カードの強さは以下の通り
# 弱 2 < 3 < 4 < ・・・・・ < 12 < 13 < 1 強

# 1.各プレイヤーは、トランプからカードを1枚選んで、自分の手札とします。
# 2.両プレイヤーは、手札を見せ合います。強いカードを持っているプレイヤーが勝ちです。
# 　なお、両プレイヤーの持っているカードの強さが同じ場合は引き分けです。

# Alice が持っているカードを A
# Bob   が持っているカードを B

# 勝敗を判定するプログラムを作る

# A B を標準入力から得る
A, B = map(int, input().split())
# print(A, B)

# Alice が 勝つなら Alice
# Bob   が 勝つなら Bob
# 引き分けなら Draw

if A == B:
    answer = "Draw"
elif A == 1:
    answer = "Alice"
elif B == 1:
    answer = "Bob"
elif A > B:
    answer = "Alice"
else:
    answer = "Bob"

# 結果を出力
print(answer)
