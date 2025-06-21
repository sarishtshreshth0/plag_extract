import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = int(lines.pop(0))
s = lines.pop(0)
count = 0
prev_c = None
for c in s:
    if c != prev_c:
        count += 1
    prev_c = c
print(count)
