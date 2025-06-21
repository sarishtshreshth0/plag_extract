import sys
n, *s = sys.stdin.read().split()
seen = set()
tmp = s[0][0]

for x in s:
    if x[0] != tmp or x in seen:
        print("No")
        sys.exit()
    else:
        seen.add(x)
        tmp = x[-1]
print("Yes")
