from sys import stdin

M, D = map(int, stdin.readline().rstrip().split())

if M < 4 or D < 22:
    print(0)
    exit(0)

cnt = 0
for i in range(21, D + 1):
    mod = i % 10
    if mod > 1 and mod * (i // 10) <= M:
        cnt += 1

print(cnt)
