import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
tree = [[] for _ in range(n)]
dic = {}

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
    dic[(a - 1, b - 1)] = i
ans = [0 for _ in range(n - 1)]
max_color = 0

def dfs(pos, before_pos, before_color):
    global max_color
    color = 1
    for next_pos in tree[pos]:
        if color == before_color:
            color += 1
        if next_pos == before_pos:
            continue
        before = min(pos, next_pos)
        after = max(pos, next_pos)
        ans_ind = dic[(before, after)]
        if pos < next_pos:
            ans[ans_ind] = color
        else:
            ans[ans_ind] = color
        max_color = max(color, max_color)
        dfs(next_pos, pos, color)
        color += 1
dfs(0, -1, -1)

print(max_color)
for i in ans:
    print(i)
