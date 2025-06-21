from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  G = [[] for _ in range(N)]
  dic = {}
  for i in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
    dic[(a, b)] = i
    dic[(b, a)] = i

  color = [0]*(N-1)
  upcol = [0]*(N)
  upcol[0] = None
  visited = set()
  q = deque([0])
  max_col = 0

  while len(q):

    now = q.popleft()
    visited.add(now)
    c = 0

    for next_ in G[now]:
      if next_ not in visited:
        c += 1
        if upcol[now] is None or not(upcol[now] == c):
          color[dic[(now, next_)]] = c
          upcol[next_] = c
        else:
          c += 1
          color[dic[(now, next_)]] = c
          upcol[next_] = c
        q.append(next_)

    max_col = max(max_col, c)

  print(max_col)
  print(*color, sep='\n')


if(__name__ == '__main__'):
  main()
