# https://atcoder.jp/contests/abc084/tasks/abc084_c
n = int(input())

trains = []
for _ in range(n - 1):
    c, s, f = map(int, input().split())
    trains.append((c, s, f))


ans = []
for i in range(n - 1):
    _c, start, _ = trains[i]
    t = start + _c
    for j in range(i + 1, n - 1):
        c, s, f = trains[j]
        if t > s:
            while t > s:
                s += f
            t += (s - t) + c
        else:
            t = s + c
    ans.append(t)
ans.append(0)
for a in ans:
    print(a)