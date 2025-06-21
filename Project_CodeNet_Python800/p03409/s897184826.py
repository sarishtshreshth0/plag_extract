import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
cd = [list(map(int, readline().split())) for _ in range(n)]
cd.sort()
cnt = 0
for c, d in cd:
    memo = []
    for i, (a, b) in enumerate(ab):
        if c > a and d > b:
            memo.append([i, b])
    if memo:
        cnt += 1
        memo.sort(key=lambda x: -x[1])
        ab.pop(memo[0][0])
print(cnt)
