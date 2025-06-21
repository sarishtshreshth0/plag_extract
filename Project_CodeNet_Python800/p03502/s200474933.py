from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

s = stdin.readline().rstrip()
point = 0

for i in s:
    point += int(i)

if int(s)%point == 0:
    print("Yes")
else:
    print("No")