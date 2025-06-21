import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import heapq

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    a_t = list(zip(*ab))
    AB = [[] for _ in range(m+1)]
    for a, b in zip(*a_t):
        if a <= m:
            AB[a].append(b*-1)
    # print(AB)
    cnt = 0
    h = [] 
    heapq.heapify(h)
    for i in AB:
        for j in i:
            heapq.heappush(h, j)
            # print('h', h)
        if h:
            cnt += heapq.heappop(h)
    print(-1*cnt)   

if __name__ == '__main__':
    main()