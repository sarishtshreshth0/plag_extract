import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
csf = [list(map(int, readline().split())) for _ in range(n - 1)]
for i, (c, s, _) in enumerate(csf):
    s += c
    for cc, ss, ff in csf[i + 1:]:
        if s < ss:
            s = ss
        elif s % ff != 0:
            s += ff - (s % ff)
        s += cc
    print(s)
print(0)
