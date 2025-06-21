import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
prv = "*"
ans = 0
for i,c in enumerate(s):
    if c!=prv:
        ans += 1
    prv = c
print(ans)