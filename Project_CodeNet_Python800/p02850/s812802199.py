from collections import defaultdict, deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    edges = [[int(i) for i in input().strip().split()] for _ in range(n - 1)]
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)

    # 1をルートとする
    que = deque([1])
    # 各頂点と親を結ぶ色を保存する
    # 1はルートのため 0 とする
    colors = [0] * (n + 1)

    # BFSで各ノードごとの子の色を決定する
    while que:
        parent = que.popleft()
        color = 0
        for child in g[parent]:
            color += 1
            if color == colors[parent]:
                color += 1
            colors[child] = color
            que.append(child)

    print(max(colors))

    for a, b in edges:
        print(colors[b])
    return


if __name__ == "__main__":
    main()
