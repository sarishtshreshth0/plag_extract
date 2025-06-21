n = int(input())
a = list(map(int, input().split()))

max_a, min_a = max(a), min(a)
cnt = [0] * (max_a + 1)
for i in range(n):
    cnt[a[i]] += 1
    if a[i] > min_a:
        cnt[a[i]-1] += 1
    if a[i] < max_a:
        cnt[a[i]+1] += 1

print(max(cnt))