S = input()
T = input()
ls = len(S)
lt = len(T)

DP = [[0] * (lt + 1) for _ in range(ls + 1)]
Ans = []
for i, s in enumerate(S, 1):
    for j, t in enumerate(T, 1):
        if s == t:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
cnts = ls
cntt = lt

while DP[cnts][cntt]:
    while DP[cnts][cntt] == DP[cnts][cntt - 1]:
        cntt -= 1
    while DP[cnts][cntt] == DP[cnts - 1][cntt]:
        cnts -= 1
    cnts -= 1
    cntt -= 1
    Ans.append(S[cnts])
print(''.join(Ans[::-1]))
