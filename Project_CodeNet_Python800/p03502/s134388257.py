import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
res = sum(list(map(int,str(n))))
if n % res == 0:
    print('Yes')
else:
    print('No')