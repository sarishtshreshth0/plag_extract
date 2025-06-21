import sys
from collections import deque
from operator import itemgetter

def read():
    return sys.stdin.readline().rstrip()

def main():
    n = int(read())
    al = [[] for _ in range(n)]
    e = dict()
    for i in range(n - 1):
        a, b = [int(j) - 1 for j in read().split()]
        al[a].append(b)
        al[b].append(a)
        e[(a, b)] = i
    v, k = 0, 0
    for i in range(n):
        if len(al[i]) > k:
            v = i
            k = len(al[i])
    print(k)
    sn = deque([(v, 0)])
    sd = set()
    ce = dict()
    while sn:
        v, cv = sn.popleft()
        sd.add(v)
        ci = 1
        for vn in al[v]:
            if vn in sd:
                continue
            if ci == cv:
                ci += 1
            if (v, vn) in e:
                ce[(v, vn)] = ci
            else:
                ce[(vn, v)] = ci
            sn.append((vn, ci))
            ci += 1
    for k, _ in sorted(e.items(), key=itemgetter(1)):
        print(ce[k])

if __name__ == '__main__':
    main()