# import sys
# input = sys.stdin.readline
s = input()
t = input()
m = len(s)
n = len(t)

D = [[0] * n for i in range(m)]
D[0][0] = int(s[0] == t[0])

for i in range(1, m):
    D[i][0] = D[i-1][0] | int(s[i] == t[0])
for i in range(1, n):
    D[0][i] = D[0][i-1] | int(s[0] == t[i])

for i in range(1, m):
    for j in range(1, n):
        mx = max(D[i-1][j-1],D[i-1][j],D[i][j-1])
        D[i][j] = max(mx, D[i-1][j-1]+1) if s[i] == t[j] else mx
# print(D)

maxl = max([max(D[i]) for i in range(m)])
# print(maxl)

ans = []
for i in range(m):
    for j in range(n):
        if D[i][j] == maxl:
            r = i
            c = j
            break

while maxl > 0:
    while c >= 1 and D[r][c-1] == maxl:
        c -= 1
    while r >= 1 and D[r-1][c] == maxl:
        r -= 1
    # print(r,c,maxl)
    ans.append(t[c])
    c -= 1
    r -= 1
    maxl -= 1
print("".join(ans[::-1]))