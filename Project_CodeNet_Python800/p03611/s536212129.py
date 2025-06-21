import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *a = map(int, read().split())
cnt = [0] * (10 ** 5 + 10)

for i in a:
    cnt[i] += 1
    cnt[i + 1] += 1
    cnt[i + 2] += 1

print(max(cnt))