import sys
from collections import deque

def read():
    return sys.stdin.readline().rstrip()

def main():
    n, m, k = map(int, read().split())
    friend = [[] for _ in range(n)]
    block = [set() for _ in range(n)]
    potential = [set() for _ in range(n)]
    for _ in range(m):
        a, b = [int(i) - 1 for i in read().split()]
        friend[a].append(b)
        friend[b].append(a)
    for _ in range(k):
        c, d = [int(i) - 1 for i in read().split()]
        block[c].add(d)
        block[d].add(c)
    sd = set()
    for u in range(n):
        if u in sd:
            continue
        sn = deque([u])
        pf = set()
        while sn:
            p = sn.pop()
            if p in sd:
                continue
            sd.add(p)
            pf.add(p)
            for f in friend[p]:
                sn.append(f)
        for pfi in pf:
            potential[pfi] = pf
    print(*[len(potential[i]) - len(block[i] & potential[i]) - len(friend[i]) - 1 for i in range(n)])

if __name__ == '__main__':
    main()