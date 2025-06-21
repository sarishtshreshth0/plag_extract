from collections import Counter as C

_ = input()
a = C([int(x) for x in input().split()])

ans = 0
for k in a:
    ans = max(ans, a[k-1] + a[k] + a[k+1])
else:
    print(ans)