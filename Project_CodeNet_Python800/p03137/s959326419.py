import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m, *x = map(int, read().split())

if n >= m:
    print('0')
    exit()

x = sorted(x)
l = sorted([x[i + 1] - x[i] for i in range(m-1)])

print(sum(l[:m-n:]))
