# AliceのスコアAとBobのスコアBを整数で入力
A,B = map(int,input().split())
# AとBが同じならDrawを出力
if A == B:
    print("Draw")
# Aが1か、Bが1でなく且つAがBより大きいならAliceを出力
elif  A == 1 or B!= 1 and A > B:
    print("Alice")
# Bの方が強ければBobを出力
else:
    print("Bob")
