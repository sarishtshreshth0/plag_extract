import bisect

n = int(input())
al = list(map(int, input().split()))
al.sort()

if n == 1:
    print(1)
    exit()
elif n == 2:
    if abs(al[0] - al[1]) <= 2:
        print(2)
        exit()
    else:
        print(1)
        exit()

ans = 0
for i in range(n):
    idx = bisect.bisect_right(al, al[i] + 2)
    tmp = idx - i
    ans = max(ans, tmp)

print(ans)
