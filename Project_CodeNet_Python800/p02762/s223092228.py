def main():
    from collections import deque
    N, M, K = map(int, input().split())
    f = [set() for _ in range(N + 1)]
    b = [set() for _ in range(N + 1)]

    for _ in range(M):
        i, j = map(int, input().split())
        f[i].add(j)
        f[j].add(i)
    for _ in range(K):
        i, j = map(int, input().split())
        b[i].add(j)
        b[j].add(i)
    
    visited = [False] * (N + 1)
    ans = [0] * (N + 1)

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        link = {i}
        todo = deque([i])
        while len(todo) != 0:
            c = todo.pop()
            for p in f[c]:
                if not(visited[p]):
                    link.add(p)
                    todo.append(p)
                    visited[p] = True
        for j in link:
            ans[j] = len(link) - len(link & f[j]) - len(link & b[j]) - 1
    
    print(*ans[1:])

if __name__ == '__main__':
    main()