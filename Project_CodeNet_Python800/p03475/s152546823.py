import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
c = [0]*(n-1)
s = [0]*(n-1)
f = [0]*(n-1)

for i in range(n-1):
    c[i], s[i], f[i] = map(int, input().split())

def dfs(eki,t):
    if eki == n-1:
        return t

    cc = c[eki]
    ss = s[eki]
    ff = f[eki]

    m = max(0,-(-t+ss)//ff)
    if t < ss:
        return dfs(eki+1, ss+cc)
    elif t%ff==0:
        return dfs(eki+1, t+cc)
    else:
        return dfs(eki+1, -(-t//ff)*ff+cc)

for i in range(n):
    print(dfs(i,0))
