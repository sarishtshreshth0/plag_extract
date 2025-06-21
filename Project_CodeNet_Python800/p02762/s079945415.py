# 2020-05-22
def main():
    n, m, k = [int(x) for x in input().split()]
    friends = [set() for _ in range(n)]
    blocks = [set() for _ in range(n)]
    for _ in range(m):
        a, b = [int(x) - 1 for x in input().split()]
        friends[a].add(b)
        friends[b].add(a)
    for _ in range(k):
        a, b = [int(x) - 1 for x in input().split()]
        blocks[a].add(b)
        blocks[b].add(a)

    networks = {}  # The dict of networks as sets. Keys are leaders.
    net_leaders = [-1] * n  # The leaders of the networks that the ones joined.
    visited = [False] * n
    for person in range(n):
        if visited[person]:
            continue
        network = set()
        stack = [person]
        while stack:
            new = stack.pop()
            visited[new] = True
            net_leaders[new] = person
            network.add(new)
            for adj in friends[new]:
                if visited[adj]:
                    continue
                stack.append(adj)
        networks[person] = network

    answers = []
    for person in range(n):
        net = networks[net_leaders[person]]
        ans = len(net) - len(friends[person]) - 1
        for block in blocks[person]:
            if block in net:
                ans -= 1
        answers.append(ans)

    print(*answers)
    return


if __name__ == '__main__':
    main()
