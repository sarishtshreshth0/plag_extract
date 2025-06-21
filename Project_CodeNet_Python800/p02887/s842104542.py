import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = ['_']+list(input())

ans = 0
for i in range(1, N+1):
    if S[i-1]!=S[i]:
        ans += 1
print(ans)