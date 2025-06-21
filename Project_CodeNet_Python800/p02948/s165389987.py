import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop, heappush 
def main():
    N, M = map(int, readline().split())
    tasks = [[] for _ in range(M)]
    for _ in range(N):
        a, b = map(int, readline().split())
        if M-a<0:
            continue
        tasks[M-a].append(b)
    s = 0
    h = []
    for i in [i for i in range(M)][::-1]:
        for b in tasks[i]:
            heappush(h, -b)
        if len(h)>0:
            s-=heappop(h)
    print(s)
if __name__ == '__main__':
    main()
