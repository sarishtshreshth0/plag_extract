def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = a[i] + s[i]
    d = {}
    for i in s:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for k in d.keys():
        ans += d[k] * (d[k] - 1) // 2
    print(ans)
resolve()