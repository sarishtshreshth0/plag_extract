import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
w = read().decode().rstrip().split()

if len(set(w)) != n:
    print('No')
    exit()
for i in range(1, n):
    if w[i - 1][-1] != w[i][0]:
        print('No')
        exit()
print('Yes')
