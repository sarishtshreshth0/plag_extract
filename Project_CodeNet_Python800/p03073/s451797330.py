import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s = instr()

prev = s[0]
ans = 0

for i in range(1,len(s)):
    if s[i] != prev:
        prev = s[i]
    else:
        ans += 1
        if s[i] == "0":
            prev = "1"
        else:
            prev = "0"

print(ans)