n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 10**5
for v in a:
    cnt[v] += 1

res = 0
for i in range(10**5-2):
    res = max(res, cnt[i] + cnt[i+1] + cnt[i+2])

print(res)