n = int(input())
w = [input() for _ in range(n)]
e = w[0][-1]
cnt = 1

for i in range(1, n):
    if w[i][0] == e:
        cnt += 1
        e = w[i][-1]

if cnt == n and len(set(w)) == n:
    print('Yes')
else:
    print('No')