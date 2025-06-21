n = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
ans = 1
while True:
    cnt1 = 0
    cnt2 = 0
    while a[i + cnt1] == a[i]:
        cnt1 += 1
        cnt2 += 1
        if i + cnt1 == n:
            ans = max(ans, cnt1)
            break
    if i + cnt1 == n:
        break
    while a[i + cnt2] <= a[i] + 2:
        cnt2 += 1
        if i + cnt2 == n:
            break
    ans = max(ans, cnt2)
    i += cnt1

print(ans)