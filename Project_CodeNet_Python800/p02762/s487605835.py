n, m, k = map(int, input().split())
friendships = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  friendships[a-1].append(b-1)
  friendships[b-1].append(a-1)
blockships = [[] for _ in range(n)]
for _ in range(k):
  c, d = map(int, input().split())
  blockships[c-1].append(d-1)
  blockships[d-1].append(c-1)
# assign users (id) for connected component, according to friendships
# also increment a counter for size of each component
component_id = [-1]*n
component_size = dict()
stack_to_visit = [(node, node) for node in range(n)]
while stack_to_visit:
  node, parent_id = stack_to_visit.pop()
  if component_id[node] != -1:
    continue
  component_id[node] = parent_id
  component_size[parent_id] = component_size.get(parent_id, 0) + 1
  for other in friendships[node]:
    stack_to_visit.append((other, parent_id))
# calculate number of suggestions for each node
for node in range(n):
  suggestions = 0
  current_id = component_id[node]
  suggestions += component_size[current_id] - 1
  suggestions -= len(friendships[node])
  suggestions -= sum(int(component_id[other] == current_id) for other in blockships[node])
  print(suggestions, end=" ")