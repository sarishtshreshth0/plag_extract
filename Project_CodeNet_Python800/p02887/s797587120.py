import sys

inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
s = instr()

prev = s[0]
ans = 1

for i in range(1,n):
    if s[i] == prev:
        continue
    else:
        prev = s[i]
        ans += 1

print(ans)
