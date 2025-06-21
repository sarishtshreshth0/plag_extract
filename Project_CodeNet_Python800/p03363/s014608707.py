n = int(input())
a = list(map(int, input().split()))

cum_a = [0]*n
cum_a[0] = a[0]
for i in range(1, n):
    cum_a[i] = cum_a[i-1] + a[i]
res = 0
cnt = {0: 0}
for cum in cum_a:
    if cum not in cnt:
        cnt[cum] = 1
    else:
        res += cnt[cum]
        cnt[cum] += 1
print(res+cnt[0])
