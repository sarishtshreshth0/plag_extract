from collections import deque

n = int(input())
rg = [[] for _ in range(n)]
ret_dict = dict()
ls = []

for _ in range(n-1):
    a, b = map(int, input().split())
    rg[a-1].append(b-1)
    rg[b-1].append(a-1)
    ls.append((a-1, b-1))


deq = deque()
deq.append((0, 0))

visited = set()
visited.add(0)

ret = 0

while deq:
    head, color = deq.pop()
    n_color = 1
    for item in rg[head]:
        if item not in visited:
            visited.add(item)
            if n_color == color:
                n_color += 1
            ret = max(ret, n_color)
            deq.append((item, n_color))
            ret_dict[(min(head, item), max(head, item))] = n_color
            n_color += 1


print(ret)
for item in ls:
    print(ret_dict[item])
