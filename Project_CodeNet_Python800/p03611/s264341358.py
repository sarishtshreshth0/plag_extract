N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (10 ** 5 + 1)

for a in A:
    cnt[a] += 1

ans = 0
for i in range(1, 10 ** 5):
    now = sum(cnt[i-1:i+2])
    ans = max(ans, now)
print(ans)

