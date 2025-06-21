#!/usr/bin/env python3
def main():
    from collections import deque

    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].add(b)
        friends[b].add(a)
    blocks = [set() for _ in range(N + 1)]
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c].add(d)
        blocks[d].add(c)

    friends_chain = []
    seen = [-1] * (N + 1)
    cnt = 0
    for person in range(1, N + 1):
        if seen[person] != -1:
            continue
        q = deque([person])
        friends_chain.append(set(q))
        while q:
            now = q.pop()
            seen[now] = cnt
            for next in friends[now]:
                if seen[next] != -1:
                    continue
                friends_chain[-1].add(next)
                q.append(next)
        cnt += 1

    for person in range(1, N + 1):
        res = friends_chain[seen[person]]
        tmp_ans = len(res) - len(friends[person]) - 1
        for block in blocks[person]:
            tmp_ans -= 1 if block in res else 0
        print(tmp_ans, end=' ')


if __name__ == '__main__':
    main()
