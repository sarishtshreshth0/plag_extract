n = int(input())

def dfs(val, A):
    if val > n:
        return
    A.append(val)
    dfs(10 * val + 3, A)
    dfs(10 * val + 5, A)
    dfs(10 * val + 7, A)

A = []
dfs(3, A)
dfs(5, A)
dfs(7, A)

cnt = 0
for v in A:
    if len(set(list(str(v)))) == 3:
        cnt += 1
print(cnt)