N = int(input())
S = input()
SL = [0]
for i in range(N):
    if S[i] == '(':
        SL.append(SL[i] + 1)
    else:
        SL.append(SL[i] - 1)

mi = min(SL)
la = SL[-1]
if mi < 0:
    S = '(' * ((-1)*mi) + S
    la -= mi
if la >= 0:
    S += ')' * la
else:
    p = (-1)*la
    S = '(' * p + S

print(S)
