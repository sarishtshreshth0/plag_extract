from collections import deque
n = int(input())
s = list(input())
d = deque(s)
l, r = 0, 0
for i in range(n):
    if l == r and s[i] == ")":
        d.appendleft("(")
    elif s[i] == ")":
        r += 1
    else:
        l += 1
s = "".join(list(d))
print(s + ")" * max(0, l - r))