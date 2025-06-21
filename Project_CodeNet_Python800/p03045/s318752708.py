from collections import defaultdict
n, m = map(int, input().split())
friends_of = defaultdict(list)#[[] for _ in range(m)]
for _ in range(m):
    x, y, _ = map(int, input().split())
    friends_of[x - 1].append(y - 1)
    friends_of[y - 1].append(x - 1)
ans = 0
visited = [False] * n
for i in range(n):
    if not visited[i]:
        ans += 1
        stack = [i]
        while len(stack) != 0:
            popped = stack.pop()
            visited[popped] = True
            for friend in friends_of[popped]:
                if not visited[friend]:
                    stack.append(friend)
print(ans)