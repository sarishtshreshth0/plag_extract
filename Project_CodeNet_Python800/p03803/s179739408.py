# 最弱 2 < ~ < 13 < 1 最強

alice_card, bob_card = map(int, input().split())

# 最強カード「1」をわかりやすく、13足して14にしとく。

if alice_card == 1:
    alice_card += 13

if bob_card == 1:
    bob_card += 13


# 勝負の処理
if alice_card == bob_card:
    print('Draw')
elif alice_card > bob_card:
    print('Alice')
elif alice_card < bob_card:
    print('Bob')