N = int(input())
a = list(map(int, input().split()))
cnt = {}

ans = 0

for v in a:
    for offset in range(-1, 2):
        val = v + offset
        if (val in cnt):
            cnt[val] += 1
        else:
            cnt[val] = 1

        if cnt[val] > ans:
            ans = cnt[val]

print(ans)