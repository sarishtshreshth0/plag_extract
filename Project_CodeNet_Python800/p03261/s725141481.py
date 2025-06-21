import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())

w = input()
last = w[-1]
past = [w]
for _ in range(N-1):
    w = input()
    if w[0] != last or w in past:
        print('No')
        quit()
    last = w[-1]
    past.append(w)
print('Yes')