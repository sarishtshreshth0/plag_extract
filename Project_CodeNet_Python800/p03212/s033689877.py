import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def dfs(a, ans):
    if a > n:
        return ans
    if set(list(str(a))) == rule:
        ans += 1
    for v in [3, 5, 7]:
        a = a * 10 + v
        ans = dfs(a, ans)
        a //= 10
    return ans


n = int(readline())

rule = set(('3', '5', '7'))
ans = 0

print(dfs(0, ans))