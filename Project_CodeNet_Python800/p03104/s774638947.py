import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, read().split())
cnt_a = []
ans = 0
check = 1
while check <= a - 1:
    x, y = divmod(a, check * 2)
    cnt_a.append(x * check + max(0, y - check))
    check *= 2
check = 1
while check <= b:
    if len(cnt_a) != 0:
        aa = cnt_a.pop(0)
    else:
        aa = 0
    x, y = divmod(b + 1, check * 2)
    cnt = x * check + max(0, y - check) - aa
    if cnt % 2 == 1:
        ans += check
    check *= 2
print(ans)
