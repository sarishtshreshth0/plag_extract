n = int(input())
weight_lists = list(map(int, input().split()))

tmp = 1000000
for i in range(1, n, 1):
    s_1 = weight_lists[:i]
    s_2 = weight_lists[i:]

    s_1_sum = 0
    for j in s_1:
        s_1_sum += j

    s_2_sum = 0
    for k in s_2:
        s_2_sum += k

    diff = abs(s_1_sum - s_2_sum)
    if diff < tmp:
        tmp = diff
        ans = tmp

print(ans)