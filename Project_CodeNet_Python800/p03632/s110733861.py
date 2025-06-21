a, b, c, d = map(int, input().split())

cnt = [0] * 101
for i in range(a, b):
    cnt[i] += 1
for i in range(c, d):
    cnt[i] += 1

ans = len(list(filter(lambda x: x == 2, cnt)))
print(ans)
