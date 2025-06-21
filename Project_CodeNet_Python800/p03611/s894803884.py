n = int(input())
a = [int(i) for i in input().split()]
if n == 1:
    print(1)
elif n == 2:
    if abs(a[0] - a[1]) <= 2:
        print(2)
    else:
        print(1)
else:
    d = {}
    for i in range(max(a) + 3):
        d[i] = 0
    for i in a:
        d[i] += 1
    ans = 1
    pre = 0
    for i in range(max(a) + 1):
        pre = d[i] + d[i + 1] + d[i + 2]
        if ans < pre:
            ans = pre
    print(ans)