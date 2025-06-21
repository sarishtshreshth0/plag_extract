
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ruiseki = [0]*(n+1)
    cnt_map = {0: 1}

    for i, a in enumerate(A):
        t = ruiseki[i] + a
        ruiseki[i+1] = t
        if t in cnt_map:
            cnt_map[t] += 1
        else:
            cnt_map[t] = 1
    ans = 0
    for cnt in cnt_map.values():
        ans += cnt * (cnt-1) // 2
    print(ans)

solve()