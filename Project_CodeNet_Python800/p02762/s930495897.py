import sys
sys.setrecursionlimit(200100)

def abc157_d():
    N, M, K = map(int, input().split())
    fr = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        fr[a].add(b)
        fr[b].add(a)
    bl = []
    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        bl.append((c,d))

    def dfs(nd, lb):
        nonlocal label, gr
        label[nd] = lb
        gr[lb] += 1
        for ch in fr[nd]:
            if label[ch] != -1: continue
            dfs(ch, lb)

    ans = [0] * N
    label = [-1] * N
    lb = 0
    gr = []
    for i in range(N):
        if label[i] != -1:
            ans[i] = gr[label[i]]
            continue
        gr.append(0)
        dfs(i, lb)
        ans[i] = gr[label[i]]
        lb += 1

    for c, d in bl:
        if label[c] == label[d]:
            ans[c] -= 1
            ans[d] -= 1

    for i in range(N):
        ans[i] -= len(fr[i]) + 1

    print(*ans, sep=' ')

abc157_d()