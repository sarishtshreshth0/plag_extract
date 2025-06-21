from collections import Counter

def main():
    n, m, k = list(map(int, input().split()))
    friendships = [tuple(map(int, input().split())) for _ in range(m)]
    blockships = [tuple(map(int, input().split())) for _ in range(k)]

    components = list(range(n))
    friends = { }

    for u, v in friendships:
        u -= 1
        v -= 1
        if u not in friends:
            friends[u] = []
        if v not in friends:
            friends[v] = []
        friends[u].append(v)
        friends[v].append(u)

    blocks = { }
    for u, v in blockships:
        u -= 1
        v -= 1
        if u not in blocks:
            blocks[u] = []
        if v not in blocks:
            blocks[v] = []
        blocks[u].append(v)
        blocks[v].append(u)

    # union-find
    cur_comp = 0
    visited = set()

    def bfs(node):
        st = [node]
        comp = node
        while st:
            n = st.pop()
            if n in visited:
                continue
            components[n] = comp
            visited.add(n)
            if n in friends:
                for nbor in friends[n]:
                    st.append(nbor)


    for u in range(n):
        bfs(u)

    hist = Counter(components)
    new_friends = [0] * n

    # for each user, look up component, calculate total
    # size of component, subtract number of users in the block
    # list that are also in that component
    for u in range(n):
        comp = components[u]
        comp_size = hist[comp]
        n_blocked = blocks[u] if u in blocks else set()
        n_friends = friends[u] if u in friends else set()
        n_same_comp = list(filter(lambda v: components[v] == comp, n_blocked))
        # print(u, n_friends, n_blocked, n_same_comp)
        new_friends[u] = comp_size - 1 - len(n_same_comp) - len(n_friends)

    print(' '.join(map(str, new_friends)))


main()
