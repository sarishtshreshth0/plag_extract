from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N, M, K = list(map(int, input().split()))

  friends = [[] for _ in range(N)]
  for _ in range(M):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

  block = [[] for _ in range(N)]
  for _ in range(K):
    a, b = map(int, input().split())
    block[a-1].append(b-1)
    block[b-1].append(a-1)

  num_cand = [-1]*(N)
  member = {}
  group = {}

  for i in range(N):
    if i in group:
      continue
    start = i
    # print(f'start:{start}')
    q = deque([start])
    member[start] = set([start])
    group[start] = start
    is_visited = set([start])
    while len(q):
      now = q.popleft()
      for next_ in friends[now]:
        num_cand[now] -= 1
        # print(f'group:{start}, now:{now}->next_:{next_}', now, '-1')
        if next_ not in is_visited:
          member[start].add(next_)
          group[next_] = start
          # num_cand[next_] -= 1
          # print(f'group:{start}, now:{now}->next_:{next_}', next_, '-1')
          # num_cand[now] -= 1
          # print(f'group:{start}, now:{now}->next_:{next_}', now, '-1')
          q.append(next_)
          is_visited.add(next_)

  # print(member)
  # print(num_cand)
  for i in range(N):
    num_cand[i] += len(member[group[i]])
    for enemy in block[i]:
      if enemy in member[group[i]]:
        num_cand[i] -= 1

  print(*num_cand, sep=' ')


if(__name__ == '__main__'):
  main()
