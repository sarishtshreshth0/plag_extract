from collections import deque
from heapq import heappop, heappush, heapify
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7


def main():
  N, M = map(int, readline().split())
  AB = [[int(x) for x in readline().split()] for _ in range(N)]
  #i日で報酬が得られるもののリスト
  days = [[0] for _ in range(M)]
  for ab in AB:
    if ab[0]-1>=M:
      continue
    else:
      days[ab[0]-1].append(ab[1])
  stack = deque(days)
  q = []
  ans = 0
  while stack:
    x = stack.popleft()
    for y in x:
      heappush(q,-y)
    z = heappop(q)
    ans += z
  print(-ans)
  
  
      
if __name__ == '__main__':
  main()