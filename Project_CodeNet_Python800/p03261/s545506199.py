import sys

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline().rstrip()
na = lambda: list(map(int, stdin.readline().split()))

# code here
N = ni()
W = []
w = input()
l = w[-1]
W.append(w)
for i in range(N-1):
    w = input()
    if w in W:
        print('No')
        break

    if not w[0] == l:
        print('No')
        break

    l = w[-1]
    W.append(w)
else:
    print('Yes')

