import sys
from collections import deque

input = sys.stdin.readline


def calc_group(N, G, group_id, group_cnt):
    g_id = 0
    for i in range(N):
        if group_id[i] != -1:
            continue
        cnt = 1
        group_id[i] = g_id
        stack = deque([i])
        while stack:
            v = stack.pop()
            for u in G[v]:
                if group_id[u] != -1:
                    continue
                cnt += 1
                group_id[u] = g_id
                stack.append(u)
        g_id += 1
        group_cnt.append(cnt)


def main():
    N, M, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        G[B].append(A)
    B = [[] for _ in range(N)]
    for i in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        B[C].append(D)
        B[D].append(C)

    group_id = [-1] * N
    group_cnt = []
    calc_group(N, G, group_id, group_cnt)

    ans = [0] * N
    for i in range(N):
        n_neighbor = len(G[i])
        n_block = sum(1 for j in B[i] if group_id[i] == group_id[j])
        ans[i] = (group_cnt[group_id[i]] - 1) - n_neighbor - n_block

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
