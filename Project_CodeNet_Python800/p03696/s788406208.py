N = int(input())
S = input()

stock = 0
L_cnt = 0
for s in S:
    if s == "(":
        stock += 1
    if s == ")":
        if stock == 0:
            L_cnt += 1
        else:
            stock -= 1

print("(" * L_cnt + S + ")" * stock)