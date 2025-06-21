n = int(input())
s = input()

L = 0  # 左かっこの数
R = 0  # 右かっこの数
cnt = 0  # 左かっこ(の数に対応した、あるべき右かっこ)の数

for i in s:
    if i == "(":
        cnt += 1
    else:
        if cnt > 0:
            cnt -= 1
        else:  # あるべき右かっこの数が０以下のとき、足りてないのは左かっこ
            L += 1
R = cnt

print("("*L + s + ")"*R)