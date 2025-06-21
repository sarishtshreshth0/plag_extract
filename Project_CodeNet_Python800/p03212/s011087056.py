def dfs(li, cnt, digits):
    if len(li) == digits:
        n = int("".join(li))
        if n <= N and all(i in li for i in ("3", "5", "7")):
            cnt += 1
        return cnt
    for i in ("3", "5", "7"):
        cnt = dfs(li + [i], cnt, digits)
    return cnt


N = int(input())
ans = sum(dfs([], 0, i) for i in range(1, len(str(N)) + 1))
print(ans)
