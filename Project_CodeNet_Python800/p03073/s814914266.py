import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = list(input())

ans1 = 0
for i, s in enumerate(S): 
    if i % 2 == 0:
        if s == "0":
            ans1 += 1
    else:
        if s == "1":
            ans1 += 1

ans2 = 0
for i, s in enumerate(S): 
    if i % 2 != 0:
        if s == "0":
            ans2 += 1
    else:
        if s == "1":
            ans2 += 1

ans = min(ans1, ans2)
print(ans)