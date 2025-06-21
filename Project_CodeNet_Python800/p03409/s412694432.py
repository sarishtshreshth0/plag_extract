n = int(input())
r = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
r.sort()
b.sort()
s = []
k = 0
ans = 0
for i in range(n):
    while True:
        if k >= n:
            break
        if b[i][0] > r[k][0]:
            s.append(r[k][1])
            k += 1
        else:
            s.sort()
            break
    for j in range(len(s) - 1, -1, -1):
        if s[j] < b[i][1]:
            ans += 1
            s.remove(s[j])
            break
print(ans)