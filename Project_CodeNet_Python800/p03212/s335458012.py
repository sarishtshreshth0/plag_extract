# 7/3

# n 以下の「753数」の個数

n = int(input())

def dfs(val):
    # 終了条件
    if val > n:
        return

    A.append(val)

    for v in [3, 5, 7]:
        val = A.pop()
        dfs(10 * val + v)
        A.append(val)

A = []
for v in [3, 5, 7]:
    dfs(v)

res = 0
for v in A:
    s = str(v)
    if '3' in s and '5' in s and '7' in s:
        res += 1

print(res)