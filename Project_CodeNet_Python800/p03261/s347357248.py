n = int(input())
s = []
fl = [[] for _ in range(n)]
ans = "Yes"
for i in range(n):
    w = input()
    if w in s:
        s.append(w)
        fl[i] = [w[0], w[-1]]
        ans = "No"
    else:
        s.append(w)
        fl[i] = [w[0], w[-1]]

for i in range(n - 1):
    if fl[i][1] != fl[i + 1][0]:
        ans = "No"
print(ans)
