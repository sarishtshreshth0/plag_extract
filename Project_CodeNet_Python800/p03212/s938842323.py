N = int(input())
ans = 0

def dfs(x, a, b, c):
    global ans
    if x > N:
        return
    if (a & b & c):
        ans += 1
    dfs(10 * x + 3, 1, b, c)
    dfs(10 * x + 5, a, 1, c)
    dfs(10 * x + 7, a, b, 1)

dfs(0, 0, 0, 0)
print(ans)
