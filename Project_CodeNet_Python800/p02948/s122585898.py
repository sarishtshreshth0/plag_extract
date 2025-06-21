import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop, heappush 
def main():
    N, M, *m = map(int, read().split())
    tasks = [[] for _ in range(M)]
    for a, b in zip(m[::2], m[1::2]):
        if M-a>=0:
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
