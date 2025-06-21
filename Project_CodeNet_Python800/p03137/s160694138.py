import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m = inintm()
X = inintl()

X.sort()
diff = []

if n >= m:
    print(0)
    exit()

for i in range(m-1):
    diff.append(X[i+1] - X[i])

diff.sort()

print(sum(diff[:m-n]))
