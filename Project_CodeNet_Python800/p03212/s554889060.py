# 再帰回数の制限緩和.
import sys
sys.setrecursionlimit(10**6)
# dfs
def dfs(s):
    ## もしsがnより大きければ、0を返す.
    if int(s)>n: return 0
    ## そうでなければ、以下を行う.
    ## cに3,5,7が一つ以上あれば、カウントは1, そうでなければ0.
    cnt = 1 if all(s.count(c) for c in '753') else 0
    ## sに対して、3,5,7を末尾に足す.
    for c in '753':
        ### s+cについてカウントを足す.
        cnt += dfs(s+c)
    return cnt

n = int(input())
print(dfs('0'))