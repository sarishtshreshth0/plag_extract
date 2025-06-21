n, a, b = map(int, input().split())
S = list(input())

count_all, count_b = 0, 0
for s in S:
    ans = "No"
    if s == "a":
        if count_all < a + b:
            ans = "Yes"
            count_all += 1
    elif s == "b":
        if count_all < a + b and count_b < b:
            ans = "Yes"
            count_all += 1
            count_b += 1
    print(ans)