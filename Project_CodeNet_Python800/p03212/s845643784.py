N = int(input())
S = str(N)
l = len(S)


ans = 0


def dfs(n):
    global ans
    if len(str(n)) == l:
        if len(set(list(str(n)))) == 3 and n <= N:
            ans += 1
        return
    else:
        if len(set(list(str(n)))) == 3:
            ans += 1

    dfs(int(str(n) + "3"))
    dfs(int(str(n) + "5"))
    dfs(int(str(n) + "7"))


dfs(3)
dfs(5)
dfs(7)

print(ans)
