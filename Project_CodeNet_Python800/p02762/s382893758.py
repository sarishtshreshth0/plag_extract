#!/usr/bin/env python3

import sys
from collections import Counter
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, M, K = map(int, readline().split())


def graph_input(N, M):
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, readline().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    return G


friend = graph_input(N, M)
block = graph_input(N, K)
seen = [0] * N


def dfs(x, group):
    # DFS で頂点 x がどの group に属するかを記録していく
    # 後に、各 group に対して、seen[x] = group となるがいくつあるか数えれば連結成分数もわかる
    seen[x] = group
    for y in friend[x]:
        if seen[y]:
            continue
        else:
            seen[y] = group
            dfs(y, group)


group = 1
for x in range(N):
    if seen[x] == 0:
        dfs(x, group)
        group += 1


counter = Counter(seen)  # リストの値の出現回数を Counter で数えることで各連結成分数を得ている

res = []
for x in range(N):
    # x 自身を連結成分数から除く-1 さらに friend[x] を除く
    cand_n = counter[seen[x]] - len(friend[x]) - 1
    # block[x]と xの連結成分の共通部分の抜くのが難しい
    for a in block[x]:
        if seen[a] == seen[x]:
            cand_n -= 1
    res.append(cand_n)

print(" ".join(map(str, res)))


if __name__ == '__main__':
    print()
