n, m = map(int, input().split())
x = list(map(int, input().split()))


x.sort()
diff = []
f = x[0]
if m <= n:
    print(0)
else:

    for i in x[1:]:
        diff.append(i-f)
        f = i

    diff.sort()
    if n == 1:
        print(sum(diff))
    else:
        print(sum(diff[:-n+1]))